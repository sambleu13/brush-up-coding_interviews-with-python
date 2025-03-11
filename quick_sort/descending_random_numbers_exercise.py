import random

# TODO: Define the 'quick_sort_desc' and 'partition_desc' functions to implement Quick Sort in descending order
def partition_desc(nums, low, high):
    pivot = nums[high]
    ind = low - 1
    for i in range(low, high):
        if nums[i] >= pivot:
            ind += 1
            nums[ind], nums[i] = nums[i], nums[ind]
    nums[ind + 1], nums[high] = nums[high], nums[ind + 1]
    return ind + 1


def quick_sort_desc(nums, low, high):
    if len(nums) == 1:
        return nums
    if low < high:
        pi = partition_desc(nums, low, high)
        quick_sort_desc(nums, low, pi - 1)
        quick_sort_desc(nums, pi + 1, high)


# Generate a list of 20 random numbers between 50 and 100
random_numbers = [random.randint(50, 100) for _ in range(20)]
print("Unsorted List: ", random_numbers)

# TODO: Use the Quick Sort function to sort the list in descending order and print the sorted list
quick_sort_desc(random_numbers, 0, len(random_numbers) - 1)
print(f"Sorted List: {random_numbers}")
