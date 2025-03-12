def evaluate_postfix_inverse(expression):
    # implement this
    list_exp = expression.split()
    stack = []
    op1 = op2 = 0
    for i in list_exp:
        if i.isdigit():
            stack.append(int(i))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if i == '+':
                result = op1 + op2
            if i == '-':
                result = op1 - op2
            if i == '*':
                result = op1 * op2
            stack.append(result)
    return stack[0]
            

print(evaluate_postfix_inverse("2 3 -"))  # Expected output: 1
print(evaluate_postfix_inverse("2 3 +"))  # Expected output: 5
print(evaluate_postfix_inverse("6 3 *"))  # Expected output: 18
