name = 'John'


def change_name():
    name = 'James'


change_name()
print(name)


def change_name():
    global name
    name = 'James'


change_name()
print(name)
