from student import Student
class HighSchoolStudent(Student):
    school_name = "High School"

    def get_name_capitalize(self):
        stuCap = super().get_name_capitalize()
        return stuCap + '-HS'

    pass