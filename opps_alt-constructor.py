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

sunny = Employee("Sunny","Instructor", 455)
rohan = Employee("Rohan", "Student", 555)
karan = Employee.from_dash("Karan-student-460")

# sunny.change_leaves(34)
# Employee.change_leaves(34)
# print(sunny.no_of_leaves)

print(karan.salary)