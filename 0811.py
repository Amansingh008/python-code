class Car:
    def setName(self, name):
        self.name = name 
    def getName(self):
        return self.name 
    
Honda = Car()
carname = input ("car name: ")
Honda.setName(carname) 
print("Honda car name:", Honda.getName())   




class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1_name = input("name of s1: ")
s1_age = input("age of s1: ")
Stud_1 = Student(s1_name, s1_age)

s2_name = input("name of s2: ")
s2_age = input ("age of student: ")

Stud_2 = Student(s2_name,s2_age)
print("Stud_1.name: ",Stud_1.name, Stud_1.age)
print("Stud_2.name: ",Stud_2.name, Stud_2.age)


class Student:
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age
        self.email = email
    
    def studentdetails(self):
        print("name", self.name, ",age", self.age, ",email", self.email)

name = input ("name: ")
age = int(input("age: "))
email = input ("email: ")
s1 = Student(name, age, email)
s1.studentdetails()


class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def employdetails(self):
        print("emoloyee name:", self.name, "employee salary:", self.salary)

name = input ("employee name: ")
salary = input("employee salary: ")
E1 = Employee(name, salary)
E1.employdetails()