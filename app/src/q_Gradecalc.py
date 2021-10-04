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


def calc_avg_grade(students: list[Student]) -> dict[int, float]:
    # Verify that the student_id is unique
    if len(students) == 0:
        return {}
   # if not is_student_unique(students):
     #   raise Exception('This student record is already in the system')

    # group by the student_id
    student_to_grades: dict[int, list[Student]] = {}
    for student in students:
        student_id: int = student.id
        if student_id in student_to_grades.keys():
            student_to_grades.get(student_id).append(student)
        else:
            student_to_grades[student_id] = [student]

    # dictionary from gradesheets that returns the grade average to a float
    student_to_grade_avg: dict[int, float] = {}
    for student_id, students in student_to_grades.items():
        grades = [x.grade for x in students]

        avg_grades = calculate_avg(grades)
        student_to_grade_avg[student_id] = avg_grades
    return student_to_grade_avg
