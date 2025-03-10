# Python program to find the temperature at which a specific coffee type is approximated to be best
import math

# Define the continuous function for the specific coffee type  
def coffee_function(T):
    return -((T - 85)**2) + 60

# Define the binary search function 
def binary_search(func, target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        # TODO: Update `left` and `right` bounds based on the `func(mid)` value
        if func(mid) < target:
            left = mid
        else:
            right = mid
    return (left + right) / 2 

# Requested precision
epsilon = 1e-6
# Identify the temperature range in which the coffee tastes the best 
temperature_range = [30, 100]

# TODO: Find the exact temperature at which your coffee tastes best.
optimal_t = binary_search(coffee_function, 30, temperature_range[0], temperature_range[1], epsilon)
print(optimal_t)
