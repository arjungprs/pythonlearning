class Student:
    school_name = "Springfield Elementary"

    def __init__(self,name,student_id=121):
        self.name = name
        self.student_id = student_id
       # student = {"name": name, "student_id" : student_id}
       # students.append(self)

    def __str__(self):
        return "Studdent" + self.name

    def get_name_capitalize(self):
        stuCap = str(self.name)
        return stuCap.upper()