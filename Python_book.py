# Write the code to find the area of circle and print the output till the 3rd decimal.

'''rad = float(input("Enter the value of radius: "))
area = 3.14 * rad * rad
print(area)
print(("{:.5f}".format(area)))  #Instead of this we can also do this>>>
ans = format(area," .3f")
print(ans)'''

#Write a program to find the hypotenuse of the right angle triangle given as ffollow: 

# as we know that = h^2 = P^2 + B^2

'''base = float(input("Enter the value of base: "))
perp = float(input("Enter the value of perpendicular: "))

hyp = base * base + perp * perp
print("The hypotenus is : ",hyp)
ans = format(hyp,".3f")
print(ans)
print("{:.3f}".format(hyp))'''

#Write a code to find the differeence betweenn the ASCII code of any latter and correspondinf upper case letter.

'''char1 = input("Enter first character: ")
char2 = input("Enter second character: ")
# print(ord(char1))
# print(ord(char2))

ord1 = ord(char1)
ord2 = ord(char2)
print("The difference off the two ASCII char is: ",ord1-ord2)'''

# print("{:,}".format(100000))

# num = eval(input('Enter the number: '))
# r1 = num % 10
# q1 = num//10
# print(num)

# Write a program to calculate the distance between two points. The formila for computing disttance is: {(x2-x1)^2 + (y2 -y1)^2}^1/2

'''x1 = eval(input("Enter x1: "))
y1 = eval(input("Enter y1: "))
x2 = eval(input("Enter x2: "))
y2 = eval(input("Enter y2: "))


result = ((x2-x1)**2 + (y2-y1)**2)
final_result = result ** 0.5
print("The distance between the two points is : ", final_result )
print("{:.3f}".format(final_result))'''

#Write a code to read two number from the user. Display the result using bitwise and operator on the numenrs.

# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# print(num1,"&",num2 ,"=", num1 & num2)

#Write a programme to read the marks of five subject through the keyword find out the aggregate and percentage of Margs obtained by the student assume maximum marks that can be obtained by a student in each subject as 100.

'''sub1 = int(input("sub1: "))
sub2 = int(input("sub2: "))
sub3 = int(input("sub3: "))
sub4 = int(input("sub4: "))
sub5 = int(input("sub5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

agree = (sub1 + sub2 + sub3 + sub4 + sub5)/5
percentage = (total_marks/500)*100
print('The agreegate is:',agree)
print("The percentage you got is: ",percentage)'''

#Write a program to read a four digit number and reverse it.

'''number = eval(input("Enter a four digit number: "))
r1 = number % 10
a1 = number // 10
r2 = a1 % 10
a2 = a1 // 10
r3 = a2 % 10
a3 = a2 // 10
r4 = a3 % 10

print("reverse is : ",r1,r2,r3,r4,sep=(""))'''

#Write a program to read a four digit number through the keyboarrd and calculate the sum of its digit;

'''number = eval(input("Enter a four digit number: "))
r1 = number % 10
a1 = number // 10
r2 = a1 % 10
a2 = a1 // 10
r3 = a2 % 10
a3 = a2 // 10
r4 = a3 % 10

print("the sum is : ",r1+r2+r3+r4)
'''

# Write programme to read the distance between any two cities in kilometres and print the distance in metre centimetre and miles

'''Dis_A_B = eval(input("Enter the distance between these two cities in km:  "))
meter = 1000
centimeter = 100000
miles = 0.6213

print("The distance in meter:",Dis_A_B*1000)
print("The distance in centimeter:",Dis_A_B*100000)
print("The distance in miles:",Dis_A_B*0.6213)'''

#Add 10 consecutive no. starting from 1 by using while loop.

'''sum = 0
i = 0
while i<=10:
    sum = sum + i
    i += 1
print(sum)'''

# Write a program to find the sum of the three digit number. 123 = 1+2+3 = 6

'''number = int(input("Enter the number: "))
sum = 0
while(number>0):
    rem = (number % 10)
    number = number // 10
    sum = sum + rem

print(sum)'''
    
# Write a program to take the 4 digit number form the user and reverse that number which is given by the user

'''n = int(input("n: "))    # Without using loop
r1 = n%10
q1 = n//10
r2 = q1%10
q2 = q1//10
r3 = q2%10
q3 = q2//10
r4 = q2%10
print("reverse: ",r1,r2,r3,r4)'''

#By using loop try to find reverse of the given number : 

'''n = int(input("Enter n: "))
rev = 0
while(n>0):
    rem = n%10
    n = n//10
    rev = rev*10 + rem
print(rev)'''

#Write a programme to print the sum of the numbers from one to twenty that are divisible by five using the while loop

'''sum = 0
i = 0
while(i<=20):
    if i % 5 == 0:
        sum = sum + i
    i = i + 1
print(sum)'''

#Write the program to print the factorial of a number by using while loop:

'''fac = 1
n = int(input("n: "))
while(n>0):
    fac = fac * n
    n = n-1
print(fac)'''

#Write the program to check the number is armstrong number or not:

'''n = int(input("Enter the number: "))
sum = 0
orig = n

while(n>0):
    sum = sum + (n%10)*(n%10)*(n%10)
    n = n//10

if sum == orig:
    print("yes armstrong numebr")
else:
    print("no")'''

'''sum = 0
for i in range(0,10,2):
    sum = sum + i
print(sum)'''

'''sum = 0
for i in range(1,20):
    if i % 2 ==0 or i % 3 == 0 or i % 5 == 0:
        pass
    else:
        print(i)
        sum = sum + i
print(sum)
'''
'''sum = 0
for i in range(0,11):
    sum = sum + i
print(sum)'''

'''n = int(input("Enter n: "))
sum = 0
n1 = 0
n2 = 1
for i in range(0,n):
    sum = n1 + n2
    n1 = n2
    n2 = sum

    print(sum,  end=" ")'''

'''for i in range(1,11,1):
    for j in range(1,6,1):
        print(format(i*j,"4d"),end=" ")'''



'''str1  = input("str: ")
l = len(str1)
print(l)
for i in range(0,l):
    if i<=4:
        print("str1:",str1[i])
    elif l<=4:
        print("string is not greater than 4")
    else:
        pass'''

# str1 = input("enter the string: ")
# str2 = input("Enter the second string: ")
# '''if str2 in str1:
#     print("True")
# else:
#     print("False")'''

# '''for i in str1:
#     if i == str2:
#         print("True")
#         break
# else:
#     print("Flase")'''

# count = 0
# flag = 0
# for i in str1:
#     if i == str2:
#         flag = 1
#     # i = i + 1
#     count = count+1
# print(count)
# # if flag == 0:
# #     print("Not")
# # else:
# #     print("yes")
        
'''str1 = input("str1: ")
str2 = input("str2: ")
count = 0
for j in str2:
    count = 0
    for i in str1:
        if j == i:
            count+=1
print("occurence: ",count)'''

#Programming Assesment:

#1. Write a programme that asks for input and prints a sequence of power of 5 from five-0 to 5n separate line.

2. # Write a program to display the number of series 149061025 two and by using for loop.

'''num = int(input("Enter the number: "))
for i in range(1,num):
    print(i*i)'''

#3. Write a program using the wild loop which prints the sum of every 5th number from 0 to 500 including both zero and 500

'''sum = 0
for i in range(0,501):
    if i % 5 == 0:
        sum = sum + i
        i = i + 1
print(sum)'''

#4. Consider a scenario where a son eats five chocolates every day the price of a chocolate is different. his father pays the bill to the chocolate vendor at the end of the every week. develop a program that can generate the bill or the chocolate and send to the father also state which loop will be used to solve this problem.

'''ch1 = int(input("ch1: "))
ch2 = int(input("ch1: "))
ch3 = int(input("ch1: "))
ch4 = int(input("ch1: "))
ch5 = int(input("ch1: "))
'''

#FUNCTION:

'''def welcome(name):
    print("Dear",name,"Welcome to the python programming")
name = input("Enter your name: ")
welcome(name)'''


'''def add(a,b,c):
    print("The sum of the given number is: ",a+b+c)

a = int(input("Enter number :"))
b = int(input("Enter number :"))
c = int(input("Enter number :"))

add(a,b,c)'''

# def default(a,b=20):
#     print(a+b)
# a = int(input("Enter number: "))
# # b = int(input("Enter number: "))

# default(a)

'''def area_of_circle(radius):
    print("The area of circle is: {:.3f}".format(radius*radius*3.14))

radius = float(input("Enter radius: "))
area_of_circle(radius)'''

# D = b^2 - 4ac

'''def discriminant(a,b,c):
    det = b*b - 4*a*c
    return det
a = eval(input("Enter a:"))
b = eval(input("Enter b:"))
c = eval(input("Enter c:"))

print("The determinant of the given function is:",b*b-4*a*c)
discriminant(a,b,c)'''

#Wrtie a program to pass the radus of a circle as a parameter to a fucntion of area of circle return the value of none if the value of hte value of th radus is negative orreturn the area of hte circle. 

'''def area_of_circle(radius):
    if radius < 0:
        print(None)
    else:
        print("The radius is: {:.3f}".format(3.14 *radius*radius))
    
radius = eval(input("Enter the value of radius: "))
area_of_circle(radius)'''

#RECUSION:

'''def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number: "))
print(fact(n))'''

#Wriote the recursive function of fibonacci series.

'''def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n = int(input("n: "))
print(fibo(n))'''

#MINI PROJECT: Calculation of compund interest and yearly analysis of interest and principal amount.
#ci = p(1+r/t)^tn - p
# p = principle amount
# r = annual interest rate
# n = numebr of years the money is invested
# t - number of ttimes the intereser of compund per year

# def comp_int(p,r,n,t):
#     print("The compound interest is:",p*(1+r/t)**(t*n)-p)

# p = int(input("Enter the principle amount: "))
# r = int(input("Enter the return interest rate : "))
# n = int(input("Enter the number of year money is invested: "))
# t = int(input("Enter the interest is compunded per year: "))

# comp_int(p,r,n,t)

# write a code to make the GCD program by using recursive method.


'''def reverse(n):
    r1 = n%10
    q1 = n//10
    r2 = q1%10
    q2 = q1//10
    r3 = q2%10
    q3 = q2//10
    r4 = q3%10
    print("the reverse : ",r1,r2,r3,r4,sep="")

n = int(input("Enter the 4 digit number: "))
reverse(n)
'''

#STRING:

# print("my name is %s and i am from  %s jharkhad"%("sunny","koderma"))
# print("my name is {} and i am from {}".format("Sunny","Jharkhand"))
# print("my name is {1} and i am from {0}".format("jharkhand","sunny"))

# list_of_company = "TCS,Microsoft,Google,speceX,Adobe,Yahoo,Amazon,Flipcart,INFOSYS"
# list1 = list_of_company.split(",")
# print(list1)
# for i in list1:
#     print(i)

#Write tue function countB which takes a word as the argument and return the umnr of b in that word.

'''def countb(str):
    print("The given string :",str)
    count = 0
    for i in str:
        if i == 'b':
            count = count + 1
    return count
str = input("Enter str: ")
print("The occurence of b:",countb(str))'''

# Write the function count later word letter which takes a word and a letter as argument and returns the number of occurrences of that letter in that word

'''def count_letter_word(word,letter):
    print(letter)
    print(word)
    count = 0
    for i in word:
        if i == letter:
            count = count+1
    return count
letter = input("Enter the letter: ")
word = input("Enter the word: ")
print("the occ of letter in word is: ",count_letter_word(word,letter))'''


#************************************** CLASS **************************************

'''class Message():
    print("welcome to opps language")
c = Message()
print(c)'''

# find the area of rectangle by using class;

'''class Rect_area():
    pass
R1 = Rect_area()

lenght = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
print("the area of rectangle is: ",lenght*breadth)'''

# calculate the area of circle:

'''class Circle():
    def area_circle(self,radius):
        self.radius = radius
        return 3.14*radius*radius
obj1 = Circle()
print("Area of circle is: ",obj1.area_circle(5))'''

# calculate the parameter of cuboid;

'''class Cuboid_para():
    def parameter(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height
        return 2*(length*breadth)+(breadth*height)+(height*length)

para = Cuboid_para()
length = int(input("Enter  len: "))
breadth = int(input("Enter  breadth: "))
height = int(input("Enter  height: "))
print("the parameter is: ",para.parameter(length,breadth,height))'''

# write a static method that checks whether all words in a list starts with a vowels or not.

'''list1 = ['axe','ludi','oranges','apple']
for i in list1:
    if i.startswith("a"or'A' or 'e' or "E" or "i" or 'I' or "o" or 'O' or "u" or "U"):
        print("yes, all words starts with vowel")
        break
    else:
        print("no, not all words starts with vowels")'''

'''class Point:
    def Set_Cordinate(self,X,Y):
        self.X = X
        self.Y = Y
    
class New_Point(Point):
    def draw(self):
        print(self.X)  
        print(self.Y)
    
p = New_Point()
p.Set_Cordinate(10,20)
p.draw()'''


'''class Point:   #base class
    def set_cordinates(self,x,y):
        self.x = x
        self.y = y
class new_point(Point):
    def draw(self):
        print(self.x)
        print(self.y) 
p1 = new_point()
p1.set_cordinates(10,20)
p1.draw()'''

'''class Sunaina:
    def details(self,height,weight):
        self.height = height
        self.weight = weight

class Sushma(Sunaina):
    def her_details(self,color):
        self.color = color
        print(self.height, self.weight, self.color)

id = Sushma()
# id.details("5ft","50kg")
id.her_details('brown')
id.her_details()
id.details()'''

'''class Box:
    height = 0
    width = 0
    depth = 0

    def __init__(self,h,w,d):
        self.height = h
        self.width = w
        self.depth = d
    def volume(self):
        return self.height*self.width*self.depth
    
class Childbox(Box):
    weight = 0
    def __init__(self, h, w, d,wt):
        self.height = h
        self.width = w
        self.depth = d
        self.weight = wt
    def volume(self):
        return self.height*self.depth*self.width
B1 = Childbox(10,20,30,150)
B2 = Childbox(5,4,2,100)
vol = B1.volume()
print("---charactersticks of the box1-----")
print("width = ",B1.width)
print("height = ",B1.height)
print("depth = ",B1.depth)
print("weight = ",B1.weight)
print("volume of the box = ",vol)

print("----charactersticks of the box2----")
print("widht = ",B2.width)
print("height = ",B2.height)
print("depth = ",B2.depth)
print("weight = ",B2.weight)
vol = B2.volume()
print("volume of the box2 = ",vol)'''

# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

'''class Vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
v1 = Vehicle(400,80)
print("Top speed of the car is:",v1.maxspeed,"\nand the mileage of this car is:",v1.mileage)'''

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.

'''class Vehicle:
    def __init__(self,color,name,brand):
        self.color = color
        self.name = name
        self.brand = brand
    def getdetails(self):
        print("The details of the bus is: ",self.name,"\n",self.color,"\n",self.brand)

class Bus(Vehicle):
    # def __init__(self, color, name, brand,mileage):
    #     self.mileage = mileage
    pass

school_bus = Bus("Yellow","Volvo","Benz")
print("The name of bus is:",school_bus.name,"The brand name is: ",school_bus.brand,"The color of bus is :",school_bus.color)'''

# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

'''class area:
    def per(self,radius):
        return 3.14 * radius * radius
    
    def perimeter(self,radius):
        return 2*3.14*radius
    
ar = area()
print(ar.per(11))
print(ar.perimeter(12))'''
        
#  Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

'''class Person:
    def setdetails(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def getage(self,age):
        self.age = age

info = Person()
print(info.setdetails()) 
'''

# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

'''class Calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        if y!= 0:
            print(x/y)
        else:
            print("cannot devide")

cal = Calculator()
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = cal.add(x,y)
print(result)
result = cal.sub(x,y)
print(result)
result = cal.mul(x,y)
print(result)
result = cal.div(x,y)
print(result)'''

#  Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

'''class Shape:
    def circleArea(self,radius):
        return 3.14* radius * radius
    def circlePer(self,radius):
        return 2*3.14*radius
    def tringleArea(self,b,h):
        return 0.5* b*h
    def tringlePer(self,b,h,l):
        return l+b+h
    def squareArea(self,a):
        return a**a
    def squarePer(self,a):
        return 4*a   
    
arper = Shape()
print(arper.circleArea(12))
print(arper.circlePer(12))
print(arper.tringleArea(12,10))
print(arper.tringlePer(12,13,14))
print(arper.squareArea(5))
print(arper.squarePer(8))'''

'''class Student():
    def __init__(self,name,age,degree):
        self.name = name
        self.age = age
        self.degree = degree

stud_1 = Student()
stud_2 = Student()

name = input("name: ")
age = int(input("age: "))
degree = input("degree: ")

stud_1(stud_1z)'''

# codetantra question: 

# class Calculator:
#     def add(self,x,y):
#         return x+y
#     def mul(self,x,y):
#         return x*y

# cal = Calculator()
# x = int(input(""))
# y = int(input(''))

# result = cal.add(x,y)
# print(result)

# result1 = cal.mul(x,y)
# print(result1)

# print("Ohhh! My \\ Goodness: ")
# print("Ohhh! My \' Goodness:\' ")
# print("Ohhh! My \n Goodness: ")
# print("Ohhh! My \t Goodness: ")
# print("Ohhh! My \f Goodness: ")
# print("Ohhh! My \r Goodness: ")
# print("Ohhh! My \b Goodness: ")

# print(format(12.3434,"10.3f"))
# print("{:.4f}".format(12.345678))

# print(format(1.00,"10.1%"))

# print("hey {} how are. you are from {}".format(25,"Jharkhand"))

# list1 = [12,23,34,45,60]
# print(min(list1))
# print(max(list1))

'''import random
list1= [10,20,30,40,50]
for i in list1:
    random.shuffle(i)
    print(i)'''


'''list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i%2 == 0:
        print(i,'even number')
    else:
        pass'''

'''print("List A = ",end="")
A = [i**2 for i in range(11)]
print(A)

print("List B = ",end="")
B = [i**3 for i in range(11)]
print(B)

print("List c the number which is even and present in A= ",end="")

C = [i for i in A if i%2 ==0]
print(C)'''

'''
print("Celcius value cel = ",end="")
print("Fehreiheit value of feh =",end="")
cel = [10,20,31.3,40,39.2]
feh = [float((cel*9/5)+32) for feh in cel]

print(feh)'''

'''l1 = [1,'x',4,5,'y',9,'m','v',0,7]
for i in l1:
    if type(l1) == int:
        print(i)
    else:
        print("Invalid")
'''

# list1 = [1,2,3,4,5,6,8]
# list1.append(89)
# print(list1)

# list2 = ['a','v','a','n','a']
# t = list2.count('a')
# print(t)

# list1 =[12,23,34,45,56]
# avg = sum(list1)/len(list1)
# print("The average of the given list is: ",avg)

# def avg_list(list1):
#     avg = sum(list1)/len(list1)
#     return avg

# list1 = [12,23,34,45,56]
# nope = avg_list(list1)
# print(nope)

'''def teble(num):
    for i in range(1,6):
        print(num,"*",i,'=',num*i)
num = int(input("Enter the numberL "))
teble(num)'''

# def even(start,end):
#     output_list = []
#     for num in range(start,end):
#         if num % 2 == 0:
#             output_list.append(num)
#     return output_list

# print((10,20))

    