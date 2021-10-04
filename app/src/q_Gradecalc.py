# Create a function called: calculate_avg_grade
# Parameters: the function should receive 1 parameter: a list of student objects
#             Remember a list can contain duplicates, so you can expect two student objects with same ID but different grades
# Returns: the function should return a dictionary with student ID as key and student average grade as value
#
# Example:
# input: [Student('s1',20,1824,90.5), Student('s2',21,1823,80.0), Student('s1',20,1824,70.0)]
# output: { 1824: 80.25, 1823: 80.0 }
#
# If the list of students is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value
from app.src.q_Student import Student
from app.src.q_Utils import calculate_avg


def calculate_avg_grade(students: list[Student]) -> dict[int, float]:
    # check if the list of students is empty, return an empty dictionary
    if len(students) == 0:
        return {}
    else:
        students: dict[int, list[Student]] = {}
# group the list by student_id
        student_to_stats: dict[int, list[Student]] = {}
        for student in students:
            student_id: int = student.id
            if student_id in student_to_stats.keys():
                student_to_stats.get(student_id).append(student)
            else:
                student_to_stats[student_id] = [student]
        student_to_avggrd: dict[int, float] = {}
# calculate average grade by student_id
        for student_id, grade in student_to_stats.items():
            grade = [x.student.grade for x in student]
            avg_grade = calculate_avg(grade)
            student_to_avggrd[student_id] = avg_grade
    return student_to_avggrd
