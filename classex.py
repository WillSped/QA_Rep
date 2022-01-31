class Students:
    def __init__(self, studentID, studentname, classname):
        self.studentID = studentID
        self.studentname = studentname
        self.classname = classname 

student = Students(23123, "Geoff", "14B")
print(student.__dict__)