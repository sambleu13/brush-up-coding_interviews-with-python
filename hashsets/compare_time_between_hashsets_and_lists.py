# check the existence of a test element in both a list and a set 100 times, 
# then print the time it took to process each case.
# Importing the necessary libraries
import time

# Define a function to demonstrate the operation and time complexity of a hash set
def compare_operations():
  
    # Create a list and a set
    data_list = []
    data_set = set()

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    # Set and List are ready; now let's define a non-existing item to search for
    test_item = 10**6 + 1  # This item is not in our set or list

    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_set` and print the result and time taken
    start_time = time.time()
    for i in range(101):
        if test_item in data_set:
            result = True
        else:
            result = False
    print(f"Hash set Test result is: {result} and took {time.time()-start_time}")
    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_list` and print the result and time taken
    start_time = time.time()
    for i in range(101):
        if test_item in data_list:
            result = True
        else:
            result = False
    print(f"List Test result is: {result} and took {time.time()-start_time}")
# Execute the function
compare_operations()
