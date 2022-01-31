from audioop import avg


class Student:
    def __init__(self, age, subject, name="student"):
        self.name = name
        self.age = age
        self.subject = subject

    def averagescore(self, score1:int, score2:int, score3:int()):
         avgscore = (score1 + score2 + score3)/3
         return avgscore   
        
        
John = Student(35, "Biology") 
Jane = Student(47, "Mathematics") 
Geoff = Student(22, "English Lit")

print("John: ", John.averagescore(78,89,57))
print("Jane: ", Jane.averagescore(98, 92, 88))
print("Geoff: ", Geoff.averagescore(78, 67, 62))



