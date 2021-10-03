name = 'John'

print(name)


def change_name():
    name = 'James'
    print(f'Name inside the function is {name}')


change_name()
print(f'Name outside the function is {name}')

name = 'John'

print(name)


def change_name():
    global name
    name = 'James'
    print(f'Name inside the function is changed to global name {name}')


change_name()
print(f'Name outside the function is {name}')
