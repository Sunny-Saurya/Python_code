'''class Employee:
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

class Player:
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game
    
    def printdetails(self):
        return f"The name is {self.name} and Game is {self.game}"
class CoolProgrammer(Employee,Player):
    language = "C++"
    def printlanguage(self):
        print(self.language)

sunny = Employee("Sunny","Instructor", 455)
rohan = Employee("Rohan", "Student", 555)

shubham = Player("Shubham",["Cricket"])
karan = CoolProgrammer("Karan",["Cricket"])'''


class electronicdevices:
        motherboard = 1
        circuit = 5

class pocketgadget(electronicdevices):
        GPS = 1
        circuit = 8
        time = "yes"

class Smartphone(pocketgadget):
        screentouch = 1
        circuit = 9
        GPU = 1
        CPU = 1

TV = electronicdevices()
ipod = pocketgadget()
apple = Smartphone()

print(apple.circuit)
print(apple.motherboard)