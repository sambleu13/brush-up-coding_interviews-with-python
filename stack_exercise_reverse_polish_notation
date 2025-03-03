# TODO: Define a function named evaluate_reverse_polish_notation that accepts an expression as a parameter
def evaluate_reverse_polish_notation(expression):
    # TODO: Initialize an empty list to act as the stack
    stack = []
    # TODO: Split the expression into tokens and iterate over them in reverse order
    clean_expression = expression.split()
    clean_expression.reverse()
    # print(clean_expression)
    for token in reversed(clean_expression):
        # print(str(token))
        # TODO: If the token is an operator ('+', '-'), pop the top two elements
        # from the stack for operation
        if token == '+' or token == '-':
            operator = token
            operand_1, operand_2 = int(stack[-1]), int(stack[-2])
            # print(str(operand_1), str(operand_2))
            stack.pop()
            stack.pop()
            if operator == '+':
                result = operand_1 + operand_2
            else:
                result = operand_1 - operand_2
            stack.append(result)
            # TODO: Based on the operator, perform the appropriate operation and push the result back onto the stack
        else:
            stack.append(token)
            # print(str(token)+'added to stack')    
        # TODO: Otherwise, treat the token as an operand and push it onto the stack
    return stack[-1]
    # TODO: Return the top element of the stack as the result of the expression evaluation

# Example usage
expression = "1 2 + 3 -"
print(evaluate_reverse_polish_notation(expression))  # Expected output: 0
