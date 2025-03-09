# TODO: Create a Python dictionary to serve as a hash table
employees = {}
# TODO: Add employee names with their roles to the dictionary
employees[1] = ['John', 'Technician']
employees[2] = ['Mary', 'Operations Manager']
employees[3] = ['Nick', 'Janitor']

# TODO: Print the initial employee database
def print_database():
    print('Employees database:')
    for id, info in employees.items():
        print(id, info)


print_database()
# TODO: Update the role of an employee in the database
employees[2] = ['Mary', 'Operations Executive']
# TODO: Print the database after the employee role update
print_database()
# TODO: Remove an employee from the database
employees.pop(1)
# TODO: Print the final employee database after the removal
print_database()
