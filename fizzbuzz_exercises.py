# coding interview question named FizzBuzz that can be solved by 
# iterating over both indices and values. In FizzBuzz, you are given a list of integers. 
# Your task is to do the following:
# Replace all integers that are evenly divisible by 3 with "fizz"
# Replace all integers divisible by 5 with "buzz"
# Replace all integers divisible by both 3 and 5 with "fizzbuzz"

def fizzbuzz(nums):
    for i, n in enumerate(nums):
        if nums[i] % 3 == 0:
            nums[i] = 'fizz'
        elif nums[i] % 5 == 0:
            nums[i] = 'buzz'
        elif (nums[i] % 3 == 0 and
         nums[i] % 5 == 0):
             nums[i] = 'fizzbuzz'
    return nums


print(fizzbuzz([45, 22, 14, 65, 97, 72]))
