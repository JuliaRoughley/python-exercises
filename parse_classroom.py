SIMPLE_CLASSROOM_PATH = "classroom_simple.txt"


def parse_simple_classroom(file_path):
    """ Parse classroom file that is given in `file_path` parameter.
    Returns a list of dictionaries describing the students in the classroom,
    each student is describe with the dictionary: {
      'name': ...,
      'country': ...,
      'grades': [...]
    }"""
    with open(file_path, 'r') as simple_classroom:
        whole_file_simple_classroom = simple_classroom.read()
        individual_students = whole_file_simple_classroom.split('###')
    students_info = []
    for student in individual_students[1:]:
        student_info = student.split('\n')
        name = student_info[1].strip('\n')
        country = student_info[2].strip('\n')
        grades = student_info[3:6]
        int_grades = []  # for converting list of grades from strings to integers
        for grade in grades:
            new_grade = int(grade)
            int_grades.append(new_grade)
        student_dict = {'name': name, 'country': country, 'grades': int_grades}
        students_info.append(student_dict)
    return students_info


def student_avg(students_list, student_name):
    """Gets input of the students_list from the above function parse_simple_classroom,
    plus the student name as second parameter, then checks for that student
    in the list of students, returns None if not found, otherwise
    calculates the average grade from the 3 grades in the grades Key of
    the student dictionary"""
    for info in students_list:
        if info.get('name') == student_name:
            return sum(info['grades']) / len(info['grades'])
    return None


def main():
    """Gets user_input of a student's name, then parses the student
    info file by running the function parse_simple_classroom, and
    passes the users input of the student name as a parameter into
    the student_avg function to get the average grade of that
    student. If student isn't in list of students, returns a polite
    error message"""
    student_name = input("Please enter a student name:")
    students_list = (parse_simple_classroom(SIMPLE_CLASSROOM_PATH))
    avg = student_avg(students_list, student_name)
    if avg is None:
        print("I'm sorry, there has been an error, please try entering the student name again.")
    else:
        print(avg)


if __name__ == "__main__":
    main()
