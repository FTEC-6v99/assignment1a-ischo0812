'''
Dictionaries
'''
# Dictionaries are a collection of key, value pairs:
employee_name_by_id = {
    1: 'John Doe',
    2: 'Jane Doe',
    3: 'James Doe'
}

# to access an item in a dictionary use the get function:
print(employee_name_by_id.get(3))  # returns John Doe
print(employee_name_by_id)

employee_name_by_id[5] = 'Mohamad Doe'
print(
    employee_name_by_id.keys())

# to loop over dictionary:
# 1. you can loop over the keys and use each key in the iteration to query the value from the dictionary:
for id in employee_name_by_id.keys():
    print(f'Employee id: {id}, Employee name: {employee_name_by_id[id]}\n')


# 2. you can loop over the values in the dictionary directly:
for name in employee_name_by_id.values():
    print(f'Employee name: {name}\n')
# 3. you can loop over the items in the dictionary, this provides you a variable reference to the key and value
# in each iteration:
for id, name in employee_name_by_id.items():
    print(f'Employee ID: {id}, Employee name: {name}\n')
