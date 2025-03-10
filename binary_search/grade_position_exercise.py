# TODO: Given a sorted list of grades in a class, implement Binary Search on this list
grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# TODO: Implement the Loop-based Binary Search function without recursion
def grade_binary_search(target, data):
    low = 0
    high = len(data)
    while high - low > 1:
        mid = (high + low) // 2
        print(data[mid])
        if target < data[mid]:
            high = mid
        else:
            low = mid
    return low if data[low] == target else None
 
        
# TODO: Set a query for a student's grade for your search
query = 100

# TODO: Invoke the Binary Search function. If you find the grade, print the position in the grade list; if not, print a not found message.
search_result = grade_binary_search(query, grades)
if search_result is not None:
    print(f"{query} is found at position {search_result}.")
else:
    print(f"{query} grade not found.")
