#What is an Object?
#An object is an instance of a class. Data members and methods of a class cannot be used directly.
# We need to create an object (or instance) of the class to use them. In simple terms, they are the actual world entities that have a state and behavior.
class Student:
 def __init__(self, studentName, studentSurname, studentRollNo):
    self.name = studentName
    self.surname = studentSurname
    self.rollNo = studentRollNo


 def getStudentDetails(self):
    print("The name of the student is", self.name, self.surname)
    print("The roll no of the student is", self.rollNo)


student1 = Student("Aarti", "Chouhan", 1)
student1.getStudentDetails()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Rohit", "Chouhan")
x.printname()

#Define encapsulation in Python
class Man:
    def __init__(self, name, child):
        self.name = name
        self.child = child

    def display(self):
        print(self.name)
        print(self.child)


man = Man('Simran', 2)  # Here we are accessing it using class method
man.display()  # Here we are accessing it directly from outside.
print(man.name)
print(man.child)

