#calulator calculator using Reverse Polish Natation (RPN)
def rpn_calculator(expression):
    stack = []
    for token in expression.split():
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
        else:
            stack.append(float(token))
    return stack.pop()

# Использование:
print(rpn_calculator("3 4 5 * +"))  # Выведет: 23.0
