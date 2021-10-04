from app.src.q_Student import Student
from app.src.q_Stats import Stats


class StatSheet():
    def __init__(self, student: Student, stats: Stats):
        self.Student = student
        self.stats = stats
