class Employee:
    no_of_leaves = 8  #global for all the object.
    
    def printdetails(self):
        return f"Name is : {self.name} Role is : {self.role} and Salary is : {self.salary}"

sunny = Employee()
rohan = Employee()

sunny.name = "Sunny"
sunny.role = "Employee"
sunny.salary = 455

rohan.name = "Sunny"
rohan.role = "Student"
rohan.salary = 4554

print(sunny.printdetails())