def days_until_cooler(temps):
    result = [-1] * len(temps)
    stack = []
    
    for i in range(len(temps) - 1, -1, -1):
        # implement this
        print(i)
        if stack:
            if temps[i] >= temps[stack[-1]]:
                result[i] = stack[-1] - i
                print(f"{stack[-1]} next is lower than {i}, output: {result[i]}")
            else:
                stack.append(i)
                print(f"{stack[-1]} is higher or equal to {i}")
        else:
            stack.append(i)
        print(stack)
    
    return result

print(days_until_cooler([30, 60, 90, 120, 60, 30]))  # Expected: [-1, 4, 2, 1, 1, -1]
print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
print(days_until_cooler([1]))  # Expected: [-1]
