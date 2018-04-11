students = []
class Student:
    school_name = "Springfield Elementary"

    def __init__(self,name,student_id=121):
        self.name = name
        self.student_id = student_id
       # student = {"name": name, "student_id" : student_id}
        students.append(self)

    def __str__(self):
        return "Studdent" + self.name

    def get_name_capitalize(self):
        stuCap = str(self.name)
        return stuCap.upper()


class HighSchoolStudent(Student):
    school_name = "High School"

    def get_name_capitalize(self):
        stuCap = super().get_name_capitalize()
        return stuCap + '-HS'

    pass

james = HighSchoolStudent("james")
print(james.get_name_capitalize())

#mark = Student("Mark")

#print(mark.get_name_capitalize())
print(Student.school_name)