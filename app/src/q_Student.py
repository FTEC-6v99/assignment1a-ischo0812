# Create a class named Student
# The Student class must extend the Person class
# In addition to the Person class attribute, the Student class must have the following attributes:
#   1. id (int)
#   2. grade (float)

from q_Person import Person

# The Student class must extend the Person class


class Student(Person):
    # Class has two attributes 1.id(int) 2.grade(float)
    def __init__(self, name: str, age: int, id: int, grade: float) -> None:
        Person.__init__(self, name, age)
        self.id = id
        self.grade = grade

    def print_name(self) -> None:
        print("ID : {2}, Name : {0}, Age : {1}, Grade : {3}".format(
            self.name, self.age, self.id, self.grade))


# p1 = Person(name='Abraham', age=31)
# p1.print_name()

# p4 = Student(name='Tommy', age=31, id=202019, grade=97)
# p4.print_name()
