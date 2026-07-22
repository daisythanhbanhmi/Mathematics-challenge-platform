# Math Challenge Arena

A web application that allows users to create, share, and solve mathematical challenges while tracking performance through a real-time leaderboard.

The project simulates the core functionality of an online learning platform where users can challenge one another with mathematical expressions, compete based on accuracy and completion time, and view rankings through a Hall of Fame system.

---

## Features

- Create and manage multiple users
- Create mathematical challenges using infix expressions
- Evaluate mathematical expressions automatically
- Send challenges to multiple users
- Attempt assigned challenges
- Record completion time for every attempt
- Hall of Fame leaderboard showing the fastest solvers
- Persistent local database using Excel

---

## Demo

### Home Page

![Home](images/home.png)

### Create Challenge

<img width="1444" height="1410" alt="image" src="https://github.com/user-attachments/assets/eeeb86e9-95f9-4844-a982-49cdd41c8e4e" />

### Attempt Challenge

<img width="1484" height="1202" alt="image" src="https://github.com/user-attachments/assets/a4dc2969-b9ec-49e6-ab73-6396f2d6972f" />

### Hall of Fame

<img width="1476" height="1256" alt="image" src="https://github.com/user-attachments/assets/43c232b4-9a79-4171-b02c-a3e6aa1c906d" />
<img width="1464" height="666" alt="image" src="https://github.com/user-attachments/assets/2a583a7d-5a28-4de8-b4ab-0c268a4e2e85" />

**Live Demo:** https://your-app.streamlit.app

---

## Technologies Used

- Python
- Streamlit
- Pandas
- OpenPyXL
- Object-Oriented Programming (OOP)
- Microsoft Excel

---

## Software Engineering Concepts

This project demonstrates:

- Object-Oriented Programming
- Stack-based infix expression evaluation
- Data persistence
- CRUD operations
- Multi-page application architecture
- Session state management
- Data processing with Pandas
- User interface development

---

## Project Architecture

```
Math Challenge Arena
│
├── Home.py
├── library.py
├── pages/
│   ├── Users
│   ├── Questions
│   ├── Challenge
│   └── Hall of Fame
│
├── Mini Project 2 - Instructor Database.xlsx
├── requirements.txt
└── README.md
```

---

## My Contributions

I developed the application, including:

- Designing and implementing the multi-page Streamlit interface
- Building an object-oriented mathematical expression evaluator
- Implementing stack-based infix expression parsing
- Managing user, question, challenge, and leaderboard data
- Reading from and writing to a local Excel database using Pandas
- Designing an interactive challenge workflow with performance tracking

---

## Installation

Clone the repository

```bash
git clone https://github.com/daisythanhbanhmi/Academic-leaderboard.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run Home.py
```

---

## Future Improvements

- User authentication
- Cloud database integration (SQLite/PostgreSQL)
- Multiplayer mode
- Difficulty levels
- Statistics dashboard
- Question categories
- Achievement badges
- AI-generated math questions

---

## License

This project is intended for educational and portfolio purposes.
