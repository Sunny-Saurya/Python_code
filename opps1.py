'''class student:
    pass

sunny = student()
lara = student()

sunny.name = "Sunny"
sunny.sub = ["Mec","mth","phy","int","cse326"]
sunny.section = "K23NC"
lara.name = "Lara"
lara.sub = ["phy","che","ece","mth"]
lara.section = "K23MC"

print(sunny.name,sunny.sub, sunny.section,sep="-")
print(lara.name,lara.sub,lara.section,sep="-")'''

class Employee:
    no_of_leaves = 8  #global for all the object.
    pass

sunny = Employee()
rohan = Employee()

sunny.name = "Sunny"
sunny.role = "Employee"
sunny.salary = 455

rohan.name = "Sunny"
rohan.role = "Student"
rohan.salary = 4554
rohan.no_of_leaves = 9 # This is instence value of no. of leaves. this is only for rohan not for sunny

#Through instence we can't change the value of class.

print(rohan.name,rohan.role,rohan.salary)
print(rohan.__dict__)
print(sunny.__dict__)
print(sunny.no_of_leaves)
print(rohan.no_of_leaves)