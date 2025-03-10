def alt_fib(n, sequence = {0: 2, 1: 3}):
    # implement this
    if n == 0:
        return 2
    elif n == 1:
        return 3
    else:
        if n not in sequence:
            sequence[n] = alt_fib(n-1, sequence) + alt_fib(n-2, sequence)
        return sequence[n]

# Test the function with some values
print(alt_fib(0))  # Expected output: 2
print(alt_fib(1))  # Expected output: 3
print(alt_fib(2))  # Expected output: 5
print(alt_fib(3))  # Expected output: 8
print(alt_fib(4))  # Expected output: 13
print(alt_fib(5))  # Expected output: 21
