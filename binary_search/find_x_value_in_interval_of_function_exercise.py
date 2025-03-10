# Python program to find the value of 'x' when f(x) = 0 using Binary Search on Continuous Space
import math

# Define a continuous function 'f'
def f(x):
    return x**3 - 5 * x**2 + 5

# TODO: Write the Binary Search Function that performs the search on the continuous function in the interval [2, 5]
def binary_search(func, target, left, right, precision):
    while right - left > precision:
        middle = (left + right) / 2
        if func(middle) < target:
            left = middle
        else:
            right = middle
    return (left + right) / 2


# TODO: Define precision, target value, and interval bounds
target = 0
left = 2
right = 5
precision = 1e-6

# TODO: Implement the binary search function and print out the value of 'x' for which f(x) is approximately 0.
x = binary_search(f, target, left, right, precision)
print(f"When f(x) = 0, x = {x}")
