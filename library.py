class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

class EvaluateExpression:
    valid_char = '0123456789+-*/(). '

    def __init__(self, string=""):
        self._expression=string

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, new_expr):
        if all(char in EvaluateExpression.valid_char for char in new_expr):
            self._expression=new_expr
        else:
            self._expression=""

    def insert_space(self):
        operators = "+-*/()"
        result = []
        for char in self.expression:
            if char in operators:
                result.append(f" {char} ")
            else:
                result.append(char)
        return "".join(result)

    def process_operator(self, operand_stack, operator_stack):
        op = operator_stack.pop()

        right = operand_stack.pop()
        left = operand_stack.pop()

        if op == '+':
            result = left + right
        elif op == '-':
            result = left - right
        elif op == '*':
            result = left * right
        elif op == '/':
            result = left / right

        operand_stack.push(result)

    def evaluate(self):
        if self.expression == "":
            return None
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()

        for token in tokens:
            if token.replace(".", "", 1).isdigit():
                operand_stack.push(float(token))
            elif token in "+-":
                while not operator_stack.is_empty() and operator_stack.peek() != '(':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)
            elif token in "*/":
                while not operator_stack.is_empty() and operator_stack.peek() in "*/":
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                while operator_stack.peek() != '(':
                    self.process_operator(operand_stack, operator_stack)

                if operator_stack.is_empty():
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()  # Remove '('



        while not operator_stack.is_empty():
            if operator_stack.peek()=="(":
                raise ValueError("Mismatched parentheses")
            self.process_operator(operand_stack, operator_stack)

        return operand_stack.pop()

