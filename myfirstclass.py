'''>What is python > Programming language , open source
>Programming > set of instruction to perform a perticular task.

>Programming Element:
1. Tokens : are smallestt individual elements of a programming elment

    K : keyword  > keywords are reserved word that has some specific meaning. KEYWORD =! VARIABLE/IDENTIFIER
    I : indentifier > is the name which is given to a variable/fuction/class etc.
    L : literals > these are the fixed value which never changes during the excution of program.
    S : seperator > there are those which seperates one element from another element.

    O : operator > are those  which perform some operator.
         1. Arithmetic operator : +,-,*,/,//
         2. Relational operator : >,<,=,!=
         3.Assignment operator : =, +=,-=,*=, /= short hand method
         4. Logical operator :  AND, OR, NOT : REVERSE THE RESULT

#COMMENT.

> MULTIPLE ASSIGNMENT : a,b,c = 3,4,5
> Python supports dynamic typing. because you do not need to put data type of any variables.'''

#1 question - Addition of two numbres.

'''a = 5
b = 6
c = a + b
print("Addition of given two number is = ",c)

# 2 question - Addition of two number by taking input from the user.

num1 = int(input("enter your first number : "))
num2 = int(input("enter your second number : "))
result = num1 + num2
print("The addition of two given number is : ", result)

> CONTROL STATEMENT : are used to control teh flow of excecution. > two parts:
 1. SELECTION CONTROL STATEMENT :
    a). if
    b). if else
    c). elif

Q. find the even number..

a = int(input("Enter the number :"))
if a % 2 == 0:
    print("even")
else:
    print("odd")

Q. find the greatest number.

2. LOOPING CONTROL STATEMENT

    a). While :
          i. initilization
          ii. condition
          iii. increment/ decreament.
Q. print a number from 1 to 10

i = 1
while i<=10:
    print(i)
    i = i + 1

3. JUMP STATEMENT
    a). break statement :
     i = 1
     while i<=10:
         print(i)
         if i == 5:
             break;
        i = i + 1

    b). continue statement :
    i = 1
     while i<=10:
         i = i + 1
         if i == 5:
             continue;
         print(i)

# DATA TYPES. :

1. LIST :  is used to store multiple elements of different types.

# there are two types of error :
1. syntax : missing of any tokens.
2. Runtime error. > if you divide any number or anything by 0 then it throughs runtime error.'''

print("I am learning","Python" ,"in" ,"INT""108")

'''Physics_marks = 80

Maths_marks = 70
Chemistry_marks = 90
Average_marks = (Physics_marks + Maths_marks + Chemistry_marks)/3
print("Average of the given score is : ", Average_marks)'''

'''phy = int(input("Enter the marks of Physics : "))
mth= int(input("Enter the marks of physics : "))
chem = int(input("Enter the marks of Chemistry : "))

average_marks = (phy+mth + chem)/3
print("The average of the given marks is : " ,average_marks)'''

'''a = 7
b = 5
if(a<b):
    print(b)
else:
    print(a)'''



#print('''Twinkle, twinkle, little star
#How I wonder what you are!
#Up above the world so high,
#Like a diamond in the sky.''')

#Character enclosed between the " " or ' ' that is called a Strings

'''x = "python"
print(x[0:3])
'''
'''L1 = [1,2,3,4,5]
L2 = ['a','b','c','d','e']
print(L1 + L2)

set = {1,2,34,5,5}
print(type(set))
'''
'''dict = {1 : "Python" , " pages" : 200}
print(dict)

dict = {"Name" : "Sunny", "Age " : 85}
print(dict)

dict = {"name" : "Python", "Code" : 108}
print(dict["Code"])'''

'''a = 10
b = 3
c = a/b
print(c)'''

'''str1 = input("Enter the string : ")
num = int(input("Enter the number : "))
dec = float(input("Enter float : "))

print("String is :", str1)
print("Integer is :", num)
print("Float is : ", dec)

print("String : %s, Integers : %d, Float : %2f",(str1,num,dec))'''


'''name = input('Enter your name :')
age = int(input("Enter your actual age : "))
dec = float(input("Enter the number in float or decimal. : "))

print("String is : %s, Integer is : %d, Float  : %.3f"%(name,age,dec))'''

'''x = 8
print(id(x)) #140711079568392

z =  8
print(id(z))'''



# Uses of operator in python.

# ARITHMATIC OPERATOR : Addition, subtraction, multiplication, division, floor and percentage division
#COMPARISION OPERATORS : =,<,>,!=
# ASSIGNMENT OPERATORS : OR SHORTHAND MATHOD.

#BITWISE OPERATORS :  If we want to represent any number in binary form we can use the bitwise operator.

# & ---> bitwise and
# || ---> bitwise or
# ~ ---> bitwise not
# ^ ---> bitwise square

# Logical operators

#if else :

'''num = int(input("Enter any number : "))

if(num % 2 == 0):
    print("Yes, this number is divisible by 2")

else:
    print("This is odd number ")
'''
# Write a program to find the greatest number :

'''num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

if num1 > num2 :
    print("the greatest number is : ",num1)

else:
    print("The greatest number is : ",num2)'''

'''num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))'''

#Write a program to find the greatest number between three numbers :

'''if num1 > num2 and num1 > num3 :
    print("the greatest number is : ",num1)

elif num2 > num1 and num2 > num3 :
    print("The greatest nuber is : ",num2)

else:
    print("The greatest number is : ",num3)
'''
# PROGRAM TO CHECK IF THE  INPUT CHAARACTER IS LOWERCASE :

'''char = input("Enter any alphabetical character : ")

if (char.islower()):  # We can also use : if(char >='a' and char <='z')
                                                        elif(char>='A' and char <='B')

    print("yes it is in lowercase")

else:
    print("it is in uppercase")'''

#WRITE A PROGRAM TO FIND WHETHER THE CHARACTER IS VOWEL OR NOT:

'''char = input("Enter the character : ")

if(char == 'a' or char ==  'e' or  char == 'i' or char ==  'o' or char ==  'u' or char == 'A' or char ==  'E' or char ==  'I' or  char ==  'O' or char == 'U'):
    print("yes it is vowel")

else :
    print("this is consonent")'''

'''branch_name = input("Enter your branch name : ")
a
if branch_name == 'CSE' or branch_name == 'ECE':
    print("You are a valid student ")

else:
    print("You are not a valid student ")'''

# Write a program to find whether the number is palindrome or not :

'''palin = input('Enter any number : ')

if palin[0] == palin[2]:
    print("yes, this is palindrome number ")

else:
    print("No, this is not a palindrome number")'''

#program to check wheather  the entered year is leap or  not. Exception : 500,1700 etc.

'''year = int(input("Enter the years : "))
if year % 4 == 0:
    print("Yes, this is a leap year")

else:
    print("No, this is not a leap year")
'''
# Another method to find the leap year:

'''year = int(input("Enter the years : "))
if year % 100 == 0 and year % 400 == 0:
    print("Yes, this is a leap year")

else:
    print("No, this is not a leap year")
'''

#Another one;
'''year = int(input("Enter any year : "))

if year % 100 == 0 and year % 400 == 0:
    print(year,"is a leap year ")

elif year % 100 != 0 and year % 4 == 0 :
    print(year, "is a leap year ")

else:
    print(year, "is not a leap year;")'''

'''marks = int(input("Enter your marks : "))

if marks >= 90 and marks < 100:
    print("You are first")

elif marks >= 80 and marks < 90:
    print("You are second")

elif marks >= 60 and marks < 80:
    print("You are third")

else:
    print("Sorry, you are fail")'''
#Write a program to print the sum of all even number:

'''n = int(input("Enter the number"))
m = 2
sum = 0
while(m<=n):
    sum = sum + m
    m += 2
print("The addition of the sum of the number 1 to 10 is : ", sum)'''

'''n = int(input("Enter the number"))
m = 1
sum = 0
while(m<=n):
    sum = sum + m
    if sum%2 == 0:
        print("The sum of the all even number : ",sum)
    m += 1
'''
# Take name and marks from the user as a input and print the marks and the name until the entered name is "end".

'''name = input("Enter your name :")
marks = int(input("Enter your marks"))
while(name!="end"):
    print("{} scored {} marks". format(name,marks))
    name = input("Enter your name :")
    marks = int(input("Enter your marks"))
else:
    print("You entered end !")'''

'''
name = input("Enter your name :")
marks = int(input("Enter your marks"))
while(name!="end"):
    print("{} scored {} marks". format(name,marks))
    name = input("Enter your name :")
    marks = int(input("Enter your marks"))
else:
    print("You entered end !")'''

'''name = input("Enter your name :")
while(name!= "end"):
    if name.isdigit():
        print("It is an integer")
    else:
        list1 = list(name)
        i = 0
        f = 0
        while i<len(list1):
            if list1[i] =="." or list1[i].isdigit():
                i = i + 1
                pass
            else:
                print(list1[i])
                f = 1
                break
if(f==1):
    print("It is a string")
else:
    print("It is a float")

name = input("Enter input: ")'''

# count the number  of digits, characters, and special character in the input.
'''
lines = input("Enter any sentance : ")
if lines.isdigit():
    print("It is a integer")
i = 0
while i<len(lines):
            if lines[i] =="." or lines[i].isdigit():
                i = i + 1
                pass
            else:
                print(lines[i])
                f = 1
                break'''

#Write a program to reverse the number accepte from user using while loop.

#Write a code or program to print the fibonacci series.

'''num = int(input("Enter the number:"))
a = 0
b = 1
print(a)
while(b<=num):
    print(b)
    temp = b
    b = a + b
    a = temp'''

'''n = int(input("Enter any number :"))
m = int(input("enter the 2nd number :"))
i = m
while(i>=1):
    if(m % i == 0 and n % i == 0):
        print(i,"is GCD")
        break
    i = i - 1'''

#Write a program to print the factor number :

'''n = int(input("Enter the number : "))
factor = []
for i in range (1,n):
    if(n%i == 0):
        factor.append(i)
print(factor)'''



