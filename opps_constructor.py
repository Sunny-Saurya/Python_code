'''class Employee:
    no_of_leaves = 8  #global for all the object.
    def __init__(self, aname, arole, asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary
    

    def printdetails(self):
        return f"Name is : {self.name} Role is : {self.role} and Salary is : {self.salary}"

sunny = Employee("Sunny","Instructor", 455)
# sunny = Employee()
# rohan = Employee()

# sunny.name = "Sunny"
# sunny.role = "Employee"
# sunny.salary = 455

# rohan.name = "Sunny"
# rohan.role = "Student"
# rohan.salary = 4554

# print(sunny.printdetails())
# print(sunny.salary)
print(sunny.__dict__)'''

class Car:
    def __init__(self, Brand, Name, Color, Price):
        self.name = Name
        self.brand = Brand
        self.color = Color
        self.price = Price

Mercedez = Car("Benz","Gwagon","Black","1.5cr")
BMW = Car("BMW","ijiff","Blue","2cr")

print(Mercedez.__dict__)
print(BMW.price)