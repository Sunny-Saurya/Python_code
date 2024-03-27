# ADD TWO NUMBER/

'''num = int(input("Enter first number"))
num1 = int(input("Enter second number"))
c = num + num1
print("The addition of the givne number is ==> ",c)'''

# FIND THE SQUARE ROOT OF THE NUMBER.

'''num = int(input("ENTER ANY NUMBER"))
print("The sqaure root of the given numebr is ==> ",num*num)'''

# FIND THE AREA OF TRIANGLE

'''base = int(input("Enter the base of the triangle"))
height = int(input("Enter the height of  the triangle"))

area = (base * height)/2
print("Area of triangle is ---> ",area)'''

# SWAP THE TWO VARIABLE

'''a = 12
b = 14
print("Before swaping ===> ",a)
print("Before swaping ===> ",b)

a,b = b,a
print("After swaping ---> ",a)
print("After swaping ---> ",b)'''

# FIND THE GREATEST AMONG THREE NUMBERS.

'''num = int(input("Enter first number"))
num1 = int(input("Enter second number"))
num2 = int(input("Enter third number"))

if(num>num1 and num1>num2):
    print("The greatest number is ", num)
elif(num1>num2 and num2>num):
    print("The greatest number is ", num1)
else:
    print("The greatest number is ", num2)'''

# FIND THE NUMBER IS PRIME OR NOT;

'''num = int(input("Enter any number"))
if num == 1:
    print("Composite number")
if num>1:
    for i in  range (2,num):
        if(num % i == 0):
            print("Composite number")
            break
    else:
        print("prime number")'''

# GENERATE A RANDOM NUMBER

'''import random
a = random.random()
print(a)

import random
b = random.randrange(1,60)
print(b)

import random
c = random.randint(10,100)
print(c)

import random
d = random.uniform(1,50)
print(d)

import random
list = [1,23,4,12,34,56,75,34,6]
num = random.choices(list)
print("Voucher of $1000 won by ==> ",num)'''

# CONVERT CELCIUS TO FAGRENHEIT

'''cel = float(input("Enter celcius"))
fah = (cel * 9/5 )+ 32
print(fah)'''

# FIND FACTORIAL OF A NUMBER

'''def fact(n):
    if(n == 0):
        return 1
    else:
        return n*fact(n-1)
x = int(input("Enter x : "))
y = fact(x)
print("{}! = {}".format(x,y))'''

#DISPLAY THE MULTIPLICATION TABLE.

'''num = int(input("Enter the number = "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    i = i + 1
'''

#PRINT FIBONACCI SEQUENCE.

'''num = int(input("Enter a number to obtain fibonacci series : "))
a = 0
b = 1

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,num + 1):
        c = a+b
        a = b
        b = c
        print(c)'''

#FIND THE ARMSTRONG NUMBER. : ---> it is only for three digit number.

'''num = int(input("Enter the number to find the armstrong number or not : "))
sum = 0
temp = num        #temporary variable

while(temp>0):
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //=  10

if(sum == num):
    print("it is an armstrong number")

else:
    print("Not a armstrong number")'''

# PRINT ARMSTRONG NUMBER WITH DIFFERENT ORDER OR DIGIT OF NUMBER THEN THIS CODE IS VALID FOR THAT. it is for multiple digit numebr

'''num = int(input("Enter the number to find the armstrong number or not : "))
order = len(str(num))

sum = 0
temp = num        #temporary variable

while(temp>0):
    digit = temp % 10
    sum = sum + (digit ** order)
    temp //=  10

if(sum == num):
    print("it is an armstrong number")

else:
    print("Not a armstrong number")'''