import streamlit as st
import pandas as pd

filename = "Mini Project 2 - Instructor Database.xlsx"

# Helper Function for Data Loading & Merging
# So now it reads the file once and stores it in memory, no need to read every time a user clicked a button
@st.cache_data
def get_leaderboard_data():
    users = pd.read_excel(filename, sheet_name='Users')
    challenges = pd.read_excel(filename, sheet_name="Challenges")
    questions = pd.read_excel(filename, sheet_name="Questions")
    
    try:
        timerecords = pd.read_excel(filename, sheet_name="Timerecord")
    except ValueError:
        # Fallback if Timerecord sheet doesn't exist yet
        return pd.DataFrame()

    if timerecords.empty:
        return pd.DataFrame()

    df = timerecords.merge(challenges, left_on='challenge_id', right_on='id')
    df = df.merge(questions, left_on='question_id', right_on='id', suffixes=('_chal', '_q'))
    df = df.merge(users, left_on='user_id', right_on='id', suffixes=('', '_user'))
    
    clean_df = df[['challenge_id', 'expression', 'answer', 'name', 'elapsed_time']].copy()
    clean_df.rename(columns={
        'challenge_id': 'Challenge No.',
        'expression': 'Question',
        'answer': 'Correct Answer',
        'name': 'User',
        'elapsed_time': 'Elapsed Time (s)'
    }, inplace=True)
    
    # Convert from 0-indexed ID to 1-indexed display number
    clean_df['Challenge No.'] = clean_df['Challenge No.'] + 1
    
    return clean_df

# --- Main App Execution ---
st.title("Improved Hall of Fame")
st.markdown("Explore challenge-specific leaderboards or view the overall global rankings.")

leaderboard_df = get_leaderboard_data()

if leaderboard_df.empty:
    st.info("No challenges have been completed yet.")
else:
    # Selection box -> Tabbed Navigation
    view_mode = st.radio("Select Leaderboard View:", ["Challenge Specific", "Overall Global Ranking"], horizontal=True)
    
    st.divider()

    if view_mode == "Challenge Specific":
        # Choose the Challenge 
        challenge_list = sorted(leaderboard_df['Challenge No.'].unique())
        selected_chal = st.selectbox("Select Challenge to View:", challenge_list)
        
        # Filter 
        chal_df = leaderboard_df[leaderboard_df['Challenge No.'] == selected_chal].copy()
        
        # Tie-Breakers (Dense Ranking) 
        chal_df['Rank'] = chal_df['Elapsed Time (s)'].rank(method='dense').astype(int)
        
        chal_df = chal_df[chal_df['Rank'] <= 3] # show only top 3
        
        chal_df = chal_df.sort_values(by='Rank')
        
        st.subheader(f"Leaderboard for Challenge {selected_chal}")
        st.caption(f"**Target Question:** `{chal_df['Question'].iloc[0]}`  |  **Solution:** `{chal_df['Correct Answer'].iloc[0]}`")
        
        display_df = chal_df[['Rank', 'User', 'Elapsed Time (s)']].set_index('Rank')
        st.dataframe(display_df, use_container_width=True)

    elif view_mode == "Overall Global Ranking":
        
        st.subheader("Global Ranking")
        
        # Count challenges solved, and sum the total time taken per user
        # Using groupby(sorter) & agg(aggregate) -> instead of using "for" loop: shorter
        global_df = leaderboard_df.groupby('User').agg(
            Challenges_Solved=('Challenge No.', 'count'),
            Total_Time_s=('Elapsed Time (s)', 'sum')
        ).reset_index()
        
        # Sort logic: Most challenges solved first, then least amount of total time taken
        global_df = global_df.sort_values(by=['Challenges_Solved', 'Total_Time_s'], ascending=[False, True])
        
        global_df['Global Rank'] = range(1, len(global_df) + 1)
        
        display_global = global_df[['Global Rank', 'User', 'Challenges_Solved', 'Total_Time_s']].set_index('Global Rank')
        
        st.dataframe(display_global, use_container_width=True)