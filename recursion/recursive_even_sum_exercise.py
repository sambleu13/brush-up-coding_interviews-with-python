def recursiveSumEven(arr, idx=0, sum=0):
    # implement this
    if idx < len(arr):
        return recursiveSumEven(arr, idx+2, sum + arr[idx])
    else:
        return sum
        

# Testing the function
print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
print(recursiveSumEven([2, 3])) # Expected output: 2
print(recursiveSumEven([])) # Expected output: 0
