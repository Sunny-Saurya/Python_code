class Employee:
    no_of_leaves = 8  #global for all the object.
    def __init__(self, aname, arole, asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary
    

    def printdetails(self):
        return f"Name is : {self.name} Role is : {self.role} and Salary is : {self.salary}"
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

class programmer(Employee):  # all the objective or gun of Employee has been taken by the programmer that is called inheritence.

    def __init__(self, aname, arole, asalary, language):
        self.name = aname
        self.role = arole
        self.salary = asalary
        self.language= language

    def printprog(self):
        return f"The programmer's name is : {self.name} Role is : {self.role} and Salary is : {self.salary} The languages are {self.language}"

# sunny = Employee("Sunny","Instructor", 455)
# rohan = Employee("Rohan", "Student", 555)
karan = programmer("Karan",666,"Programmer","C, C++, Python")
print(karan.printprog())
print(karan.printdetails())