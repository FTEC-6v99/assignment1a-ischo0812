# Create a new class called Person
# The Person class must have two attribues:
#   1. name (str)
#   2. age (int)

class Person:
    # Class has two attributes 1.name(srt) 2.age(int)
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def print_name(self) -> None:
        print(f'{self.name} {self.age}')


# p1 = Person(name='Abraham', age=31)
# p1.print_name()
# p2 = Person(name='William', age=35)
# p3 = Person('Johnson', 25)
