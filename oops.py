# code
class Student:
 def __init__(self, studentName, studentSurname, studentRollNo):
    self.name = studentName
    self.surname = studentSurname
    self.rollNo = studentRollNo


 def getStudentDetails(self):
    print("The name of the student is", self.name, self.surname)
    print("The roll no of the student is", self.rollNo)


student1 = Student("Aarti", "Chouhan", 22)
student1.getStudentDetails()