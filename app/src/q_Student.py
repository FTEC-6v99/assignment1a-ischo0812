# Create a class named Student
# The Student class must extend the Person class
# In addition to the Person class attribute, the Student class must have the following attributes:
#   1. id (int)
#   2. grade (float)

from q_Person import Person


class Student(Person):
    def __init__(self, name: str, age: int, id: int, grade: float) -> None:
        Person.__init__(self, name, age)
        self.id = id
        self.grade = grade

        print("ID : {2}, Name : {0}, Age : {1}, Grade : {3}".format(
            self.name, self.age, self.id, self.grade))


p1 = Person(name='Abraham', age=31)

p4 = Student(name='Tommy', age=31, id=202019, grade=97)
p5 = Student(name='Michael', age=35, id=202025, grade=93)
p6 = Student('Adam', 36, 202066, 90)
