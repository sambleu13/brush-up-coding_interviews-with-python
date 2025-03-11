def sort_sales(sales):
    # implement this
    return sorted(sales, reverse = True)

print(sort_sales([10, 15, 4, 20, 1])) # Expected: [20, 15, 10, 4, 1]
print(sort_sales([30, 25, 20, 15])) # Expected: [30, 25, 20, 15]
print(sort_sales([3, 8, 5])) # Expected: [8, 5, 3]
