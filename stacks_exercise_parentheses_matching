# Complete the function to properly use stack operations for parenthesis matching
def is_valid_expression(expression):
    stack = []
    is_valid = True
    open_paren = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        #print(str(char))
        if char in '([{':
            stack.append(char)
            #print(str(char)+'added to stack')
        elif char in ')]}':
            # TODO: Determine if the stack is empty OR the last character does
            # not match the corresponding opening character
            #print(str(char)+'comparing to last item in stack')
            if char in open_paren:
                if not stack:
                    #print('empy stack')
                    is_valid = False
                else:
                    #print(str(stack[-1])+'deleted from stack')
                    stack.pop()
                    is_valid = True
        # TODO: What to do if the `char` is not a parenthesis?
        
    # TODO: Check if the stack is empty, indicating that the expression is balanced
    if stack:
        is_valid = False
    
    return is_valid  # Modify this line appropriately


# Example usage
sample_expression = "([a+b]{c+d})"
print(is_valid_expression(sample_expression))  # Expected output: True

bad_expression = "([a+b]{c+d}))"
print(is_valid_expression(bad_expression))  # Expected output: False
