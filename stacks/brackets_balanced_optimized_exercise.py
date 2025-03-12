def are_brackets_balanced(s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_brackets = set(["(", "[", "{"])
    stack = []
    # implement this
    for char in s:
        if char in ('(){}[]'):
            if char in open_brackets:
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
            

print(are_brackets_balanced("(abc[d]{fg})"))  # Expected output: True
print(are_brackets_balanced("(a[bcd{fg}h]i)"))  # Expected output: True
print(are_brackets_balanced("(abc{d[fg]h)i"))  # Expected output: False
print(are_brackets_balanced("({a[bcd]})"))  # Expected output: True
