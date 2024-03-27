# Function practice question : 

#1. write a program of addition by using function:

'''def addition(a,b):
    print("The sum of two number is:",a+b)

addition(12,23)'''

#  take input from the user;

'''def addition(a,b):
    print("The sum of two number is:",a+b)

a = int(input("enter first number: "))
b = int(input("enter second number : "))

addition(a,b)'''

# def addition(a,b = 3):
#     print("The sum of two number is:",a+b)

# addition(12)

'''def test1(a,b,c):
    return a,b,c

tup = test1("sunny","kumar",19)
print(tup)'''

'''def test2(a = "sun" , b = "sunny"):
    return a,b

lets = test2("sidhu","moosewala")
print(lets)'''

'''def test3(list1):
    for i in list1:
        print(i)

list1 = input("Enter the no. of list: ")
test3(list1)'''


# Stericks of args:  * this is used for taking too much variable. its upto you that how much you take. for eg. args in not a keyword.

'''def test5(*a): 
    return a

tup =(12,23,34)
print(tup)'''

#double stericks: this is used for taking key and value pair.

'''def test6(**kwargs):
    return kwargs

dict = test6(name = "sunny",email_id = "sunnysaurya@gamil.cone", ph_no = "7667640003")
print(dict)'''

# 2. Write a Python function to sum all the numbers in a list.

'''def sum_list1(num):
    sum = 0
    for i in num:
        sum = sum + i
        # i = i + i
    return sum 
print(sum_list1((2,3,4)))  '''  


'''def mul_list1(num):
    mul = 1
    for i in num:
        mul = mul * i
    return mul

print(mul_list1((2,3,4)))'''

'''def reverse_str(num):
    reversed = num[::-1]
    return reversed

print(reverse_str(("1234abcd")))'''

'''def facto(num):
    if num == 0:
        return 1
    
    else:
        fact = num * facto(num - 1)
        return fact

print(facto((6)))'''

# def in_range(num):
#     if num in range(0,21):
#         print("yes this no. falles in this range")
#     else:
#         print("No, this no. is not falls in this range")

# print(in_range((22)))


#********************************CLASSS QUESTIONS AND CONCEPT *********************************88

'''class user_details():
    def __init__(self,username,password,followers):
        self.username = username
        self.password = password
        self.followers = followers
    
    def show_username(self):
        print("His username is :",self.username)

Ram = user_details("ram@123",45678,"12k")
Rohan = user_details("rohan_123",98765,"18k")

Ram.show_username()
Rohan.show_username()'''

# print(Ram.username,Ram.password,Ram.followers)
# print(Rohan.username,Rohan.password,Rohan.followers)


#*************************INHERITENCE****************************

'''class my_parents:
    def __init__(self,color,brain,nature):
        self.color = color
        self.brain = brain
        self.nature = nature

    def I_inherit_from_myparents(self):
        print(f"I get my color form {self.color} I get my brain form {self.brain} and I get my nature form{self.nature} from my whole family")

class mein_khud(my_parents):
    def my_details(self):
        print("I inherit my whole nature skin nature and brain from my parents")

sunny = mein_khud("mother", 'father', "both")
print(sunny.brain)
print(sunny.nature)
print(sunny.color)
sunny.I_inherit_from_myparents()
sunny.my_details()'''

# print("Hello World")
# print("Hey everyone !")
# num = 1
# num2 = 4
# print(num + num2)
# s = {1,2,3,4,5,6}
# print(type(s))
# d = {"good": "Ohh my goodness", "cool": "Hello hello ", "Yt name": "Sunny Saurya"}
# print(type(d))
# print(d)
# print(d.get("Yt name"))

# age = int(input("Enter your age: "))
# match age:
#     case 1:
#         print("Number 1")
#     case 2:
#         print("Number 2")
#     case 3:
#         print("Number 3")

#write a python program to print the table of any numbe which is lies between the 1- 10.

# num = int(input("Enter a number: "))

# match num: 
#     case 1:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 2:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 3:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 4:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 5:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 6:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 7:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 8:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 9:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)
#     case 10:
#         for i in range(1,11):
#             print(num,"X",i,"=",num*i)

# print("Enter a valid number that lies between 1 - 10")
# print("End of the program")


#FUnCtion  in python

# def letter_to_mam(name,date):
#     st =  f"Hello mam, This is {name} i will not come to school at {date}"
#     print(st)
# letter_to_mam("sunny","26th october")


# Prime number by using python

# num = int(input("Enter number to check the prime number: "))
# if num == 1:
#     print("Not a prime number")
# if num>1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")

# import random
# print("Random Number Between 1-10 : ")
# num = random.randint (1,10)
# if num == 7:
#     print("Hurray, you won the lottery")
# else:
#     print("Sorry, you lost the lottery")
# print(num)


#print the all prime number between the interval of 1-100:

# lower = int (input("Enter the lower range: "))    
# upper = int (input("Enter the upper range: "))    
# for num in range(lower, upper+1):
#     if num>1:
#         for i in range(2,num):
#             if num % i == 0:
#                 print(f"{num} not prime ")
#                 break
#         else:
#             print(f"{num} prime ")


# num = int(input("Enter any number to check the factorial of that numeber: "))
# fac = 1
# if num == 0 or num == 1:
#     print("factorial is 1")
# for i in range(1,num+1):
#     fac = fac*i
# print(fac)


# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num* factorial(num-1)
# num = int(input("Enter a non zero positive integer: "))
# result = factorial(num)
# print(result)

# m = 0
# n = 1
# num = int(input("Enter any number: "))
# if num == 1:
#     print(m)
# else:
#     for i in range(0,num+1):
#         c = m+n
#         n = m
#         m = c
#         print(c)


# Fro armstrong number;

num = int(input("Enter no. to check the armstrong number: "))
temp = num
sum = 0

while(temp>0):
    digit = temp % 10
    cube = digit **3
    sum = sum + cube
    temp =temp//10
if sum == num:
    print("Yes, armstrong number")
else:
    print("Not, armstrong number")

