'''print("Hello World")

sum = 0
n = 1
while(n<=10):
    sum = sum + n
    n = n + 1
    print(sum)

items = list(range(1,11))
for i in items:
    if(i % 2 == 0):
        print(i,"even number")
    else:
        print(i,"odd number")

n = 1
while(n<=100):
    if(n % 2 == 0):
        print(n,"even number")
    else:
        print(n,"odd number")
    n = n+1

number = int(input("Enter any number to know the table"))
i = 1
while(i<=10):
    print(number,'*',i ,'=', number * i)
    i = i + 1'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print("\n")'''

'''i = 0
while(i<=6):
    j = 1
    while(j<=i+1):
        print(j,end = " ")
        j = j+1
    print("\n")
    i = i + 1'''

'''num = list(range(1,55))
for i in num:
    print(i,"even number")
    if(i == 50):
        continue;
else:
    print(i,"odd number")'''

'''str = "python"
for i in str:
    print(i)
    if(i == 'h'):
        break;
else:
    print(i)'''

'''str = "python"
for i in str:
    print(i)
    if(i == 'h'):
        continue;
else:
    print(i)'''

'''num = int(input("Enter any number"))
if(num % 7 == 0):
    print(num,"is divisible by 7")
else:
    print(num,"is not divisible by 7")'''

'''num = int(input("Enter any number"))
if(num % 5 == 0):
    print("hello")
else:
    print("bye")'''

# ********************************************************************************************************************

# PRINT THE FIBONACCI SERIES

'''num = int(input("Enter the number of term : "))
a = 0
b = 1

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,num+1):
        c = a+b
        a = b
        b = c
        print(c)'''

'''num = int(input("Enter the three digit number"))
sum = 0
temp = num

while(temp>0):
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10

if(sum == num):
    print("Yes, it is an armstrong number")

else:
    print("No,it is not an armstrong number")'''

#FOR MULTIPLE DIGIT OR NUMEBR

'''num = int(input("Enter the number here : "))
order = len(str(num))

sum = 0
temp = num

while(temp>0):
    digit = temp % 10
    sum = sum + (digit ** order)
    temp = temp // 10

if(sum == num):
    print("Yes, it is an armstrong number")

else:
    print("No, it is not an armstrong number")'''

'''number = int(input("Enter the number : "))
last_digit = number // 10

if last_digit  % 3 == 0:
    print("Yes, it's last digit number is divisible by 3")

else:
    print("No, the last digit is not divisble by 3")'''

'''price_of_bike = int(input("Enter the price of the bike : "))
road_tax = 0

if price_of_bike > 100000:
    road_tax =  (price_of_bike * 15/100)
    print("The tax is : " ,road_tax)

elif  price_of_bike > 50000 and price_of_bike <= 100000:
    road_tax = price_of_bike * 10/100
    print("The tax is : " ,road_tax)

else:
    road_tax = price_of_bike * 5/100
    print("The tax is : " ,road_tax)'''

#Write a program to check whether it is leap year or not.

'''year = int(input("Enter the year : "))

if year % 4 == 0:
    print("Yes, it is a leap year")

else:
    print("No, it is not a leap year")'''

# Write a program to wheather a number is divisible by 2 and 3 .

'''number = int(input("Enter the number : "))
if number % 2 == 0 and number % 3 == 0:
    print("Yes, this number is divisivble by both 2 and 3")

else:
    print("No, this number is not divisible by 2 and 3")'''

# Write a program to find the number is negetive or positive or zero.

'''number = int(input("Enter the number : "))

if number < 0:
    print("This number is negative number ")

elif number == 0:
    print("this number is zero")

else:
    print("this number is positive number ")'''

#write a program and accept the age of 4 people and display the youngest one

'''age1 = int(input("Enter your age :"))
age2 = int(input("Enter your age :"))
age3 = int(input("Enter your age :"))

if age1 < age2 and age1< age3 :
    print("The youngest one is ", age1)

elif age2 < age1 and age2 < age1:
    print("The youngest one is ", age2)

else:
    print("The youngest one is ", age3)'''

'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num4

if(f1>f2):
    print(f1,"is the greatest number")

else:
    print(f2,"is the greatest number")'''
'''
user_name = input("Enter your user name: ")
len = len(user_name)
print(len)

if(len>10):
    print(user_name,"this contain more than 10 charater. ")
else:
    print(user_name, "This contain less than 10 chracter")'''

'''name = ['sunny','baasu',"ayush",'harry','vishal','rohit','mohit']
if('khandu don' in name):
    print(True)
else:
    print(False)'''

#print the numer from 1 to 50

'''i = 1
while(i<50):
    print(i)
    i += 1'''
'''
list = [1,3,4,5,6,7,8,6,5,4,3]
for i in list:
    print(i)'''

'''fruits = ['banana','watermelon','dragon fruits','oranges','mangoes']
i = 0
while(i<len(fruits)):
    print(fruits[i])
    i = i +1'''

'''num = int(input("Enter any number that you want to kneo the table: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)'''
'''
num = int(input("Enter any number: "))
i =1
while(i<11):
    print(num,'*',i,'=',num*i)
    i = i+1'''

'''list = ['sunny','rohit','basu','prabhutee','mansimran']
for i in list:
    print("good mornig",i)'''

#Write a program to print wheteher the given number is prime or not.
'''num = int(input("Enter any number: "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print(num,"is prime number")
else:
    print(num,"is composite number")'''

'''num = int(input("Enter any number: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial *i
print(factorial)'''

'''num_line = int(input("Enter no. of line: "))
for i in range(num_line):
    print("*" * ( i+1))'''

'''n = int(input("enter no. of lines: "))
for i in range(n):
    print(" " * (n-i-1), end = "")
    print("*" * (2*i+1), end = "")
    print(" " * ( n-i-1))'''

'''a,b = 4,6
c = a if(a%2 == 0) else b
print(c)

[print(a*b) for a in [1,2,3] for b in [10,20,30]]

[print(a) for a in {10, 8, 5, 4} for b in {4, 7, 5, 10}if a == b]
[print(a*7) for a in range(1,11) if (not a*7 == 42)]

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

L1 = [a for a in range(n1,n2) if(a%2 == 0 and a%3 == 0)]
print(L1)'''

'''x= int(input("x: "))
y = int(input("y: "))
i = y
while(i>=1):
    if(y % i == 0 and x % i == 0):
        print(i,"is GCD")
        break
    i = i - 1'''

'''n = int(input("Enter the number you want oto fidn the armsstong number of: "))
orig = n
sum = 0
while n>0:
    sum = sum + (n%10)*(n%10)*(n%10)
    n = n//10

if orig == sum:
    print("This is an armstrong number")
else:
    print("This is not the armstrong number")'''

class Student:
    pass

Student.name = "Sunny"
Student.section = "K23NC"

print(Student.name)