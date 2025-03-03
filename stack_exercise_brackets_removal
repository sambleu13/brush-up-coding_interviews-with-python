# Create a function that determines the minimum number of bracket removals needed for a valid string.

def min_removals_to_balance(brackets):
    # TODO: Initialize an empty list to act as the stack
    stack = []
    removals = 0
    # TODO: Iterate through each bracket in the input string
    for char in brackets:
        print(str(char))
        if char == '(':
            stack.append(char)
            print(str(char)+'added to stack')
        elif char == ')':
            if stack:
                if stack[-1] == '(':
                    print('valid ()'+str(stack[-1])+'removed')
                    stack.pop()
                elif stack[-1] == ')':
                    removals += 1
                    print('invalid ()'+str(stack[-1])+'removals updated = '+ str(removals))

            else:
                removals += 1
                print('invalid (), empty stack removals updated = '+ str(removals))
                
        # TODO: Add conditions to handle the opening and closing brackets
        # appropriately using stack operations
    if stack:
        print(str(stack))
        removals +=1 
    # TODO: Return the count of brackets that need to be removed to make the
    # string valid
    return removals
 
    
# Example usage
invalid_parentheses = "()))(()"
removals_needed = min_removals_to_balance(invalid_parentheses)
print(removals_needed)  # Expected output: 3
