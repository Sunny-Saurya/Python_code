# ADDITION PROGRAM BY USING FUNCTIONS.
# its is same as in subtraction, multiplication, division and module function.
'''def addition(num1, num2):
    sum = num1 + num2
    return sum

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number : "))
result = addition(num1, num2)
print(result)'''

# WRITE A ODDEVEN PROGRAM BY USING FUNCTIONS

'''def evenodd(number):
    if number % 2 == 0:
        print(number,"is an even number")
    else:
        print(number,"is an odd number")

number = int(input("Enter the number to check : "))
evenodd(number)'''

# WRITE MAX MIN PROGRAM BY USING FUNCTIONS.

'''def maxmin(num1, num2):
    if num1 > num2:
        print(num1,"is the greatest number")
    else:
        print(num2,"is the greatest number")

num1 = int(input("Enterr the first number : "))
num2 = int(input("Enter the second number :"))
maxmin(num1,num2)'''

# WRITE NAGETIVE,POSITIVE NUMNER BY USING FUNCTIONS.

'''def posinegi(number):
    if number > 0:
        print(number, "is positive number")
    elif number < 0:
        print(number,"is negetive number")
    else:
        print(number, "is zero")

number = int(input("Enter the number :"))
posinegi(number)'''

# PRINT FROM 1 TO 100

'''def onetohun():
    i = 0
    while i<=100:
        print(i)
        i = i + 1
onetohun()'''

# BY TAKING INPUT FRO M THE USER.

'''def onetonum(number):
    i = 0
    while i <= number:
        print(i)
        i+=1

number = int(input("Enter your number"))
onetonum(number)'''

# PRINT THE SUM 0F FIRST TEN NATURAL NUMBER.

'''def natural():
    i = 0
    sum = 0
    while i <= 10:
        sum = sum + i
        i = i + 1
    print(sum)

natural()'''

# TAKE THE NUMBER FROM THE USER AND PRINT THE SUM

'''def natural(number):
    i = 0
    sum = 0
    while i <= number:
        sum = sum + i
        i = i + 1
    print(sum)

number = int(input("Enter the number to find the sum :"))
natural(number)'''

# WRITE A PROGRAM TO FIND THE SUM OF DIGIT OF A GIVEN NUMBER BY USING FUNCTION.

'''def sum_of_digit(number):
    sum = 0
    while number >0:
        sum = sum + (number % 10)
        number = number // 10
    print(sum)

number  = int(input("Enter the three digit number : "))
sum_of_digit(number)'''

# WRITE A PROGRAM TO FIND THE MULTIPLICATION OF DIGIT OF A GIVEN NUMBER BY USING FUNCTION

'''def mul_of_digit(number):
    mul = 1
    while number > 0:
        mul = mul * (number % 10)
        number = number // 10
    print(mul)

number = int(input("Enter the number you want to multiply: "))
mul_of_digit(number)'''

# NOW DO THE SUM AND MUL TOGETHER.

'''def sum_mul(number):
    sum = 0
    mul = 1
    while number>0:
        sum = sum + (number % 10)
        mul = mul * (number % 10)

        number = number // 10
    print(sum)
    print(mul)

number = int(input("Enter the number to check : "))
sum_mul(number)'''

# WRITE A PROGRAM TO SUM OF EVEN AND PRODUCT OF ODD DIGIT OF A GIVEN NUMBER.

'''def sumeve_prood(number):
    sum = 0
    pro = 1
    while number > 0:                            #WRONG
        digit = 0
        digit = number % 10
        if digit % 2 == 0:
            sum = sum +digit

        else:
            pro = pro * digit

        number = number //10

        print("sum of the even digit is : ",sum)
        print("pro of the odd digit is : ",pro )

number = int(input("Enter the number to check : "))
sumeve_prood(number)'''

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd

'''def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return a
    else:
        return b

even = lesser_of_two_evens(2,4)
print(even)
odd = lesser_of_two_evens(2,5)
print(odd)'''

# Write a function takes a two-word string and returns True if both words begin with same letter

'''def animal_crackers(a):
    if 0 == 6:
        return True
    else:
        return False

result = animal_crackers('Sunny Sania')
print(result)'''

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False

'''def makes_twenty(a,b):
    if  a == 20 or a + b == 20:
        return True
    else:
        return False

a = makes_twenty(11,9)
print(a)
b = makes_twenty(12,21)
print(b)'''

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

#Write a function that computes the volume of a sphere given its radius.

'''def volume(radius):
    vol_of_sphere = (4 * 3.14 * (radius**3)) / 3
    return vol_of_sphere

radius = int(input("Enter the value of radius :" ))
result = volume(radius)
print(result)'''

#Write a function that checks whether a number is in a given range (inclusive of high and low)

'''def ran_check(num, low, high):
    if num < high and num > low:
        print(num, " is in a range of ", low ,"and", high)

    else:
        print(num,"is not in a range of ",low ,"and" ,high)

num = int(input("Enter the number :"))
low = int(input("Enter the lowest range of the number :"))
high = int(input("Enter the highest range of the number :"))

ran_check(num,low,high)'''

#If you only wanted to return a boolean:

'''def ran_check(num, low, high):
    if num < high and num > low:
        return True

    else:
        return False

num = int(input("Enter the number :"))
low = int(input("Enter the lowest range of the number :"))
high = int(input("Enter the highest range of the number :"))

result = ran_check(num,low,high)
print(result)'''

# Write a Python function that accepts a string and calculates the number of
# upper case letters and lower case letters.

'''def upper_lower_case(str):
    dict = {"upper": 0, "lower": 0}
    for case in str:
        if case.isupper():
            dict["upper"] += 1

        elif case.islower():
            dict["lower"] += 1

        else:
            pass

    print("Original String : ", str)
    print("No. of Upper case characters : ", dict["upper"])
    print("No. of Lower case Characters : ", dict["lower"])

str = 'Hello Mr. Rogers, how are you this fine Tuesday?'
upper_lower_case(str)'''

#Write a Python function that takes a list and returns a new list with unique elements of the first list

'''def unique_list(list):
    x = []
    for a in list:
        if a not in x:
            x.append(a)
    return x

list = [1,1,2,3,3,3,4,4,5,5,6,7,1,1,1,2,2,3]
result = unique_list(list)
print(result)
list = [1,2,3,4,4,4,5,6,6,7,8,9,0]
result_1 = unique_list(list)
print(result_1)'''

# Write a Python function to multiply all the numbers in a list.

'''def multiply_total(list):
    pro = 1
    for a in list:
        pro *= a
    return pro
list = [2,4,6,2]
result = multiply_total(list)
print(result)'''

# Write a Python function that checks whether a word or phrase is palindrome or not.

'''def palindrome(str):
    str = str.replace(' ','')   # This replaces all spaces ' ' with no space ''
    return str == str[::-1]

str = "nurses run"
str1 = "abcda"
result = palindrome(str)
print(result)
result1 = palindrome(str1)
print(result1)'''

# Write a Python function to find the maximum of three numbers.

'''def maximum(a,b,c):
    if a>b and a>c:
        print("Max no. is: ",a)
    elif b>a and b>c:
        print("Max no. is:",b)
    else:
        print("Max no. is:",c)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c "))
maximum(a,b,c)'''

# Write a Python function to sum all the numbers in a list.

'''def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))'''

# Write a Python function to multiply all the numbers in a list.

'''def sum(numbers):
    mul = 1
    for x in numbers:
        mul *= x
    return mul
print(sum((8, 2, 3, 7)))'''

# Write a Python program to reverse a string.

'''def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))'''

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''
def fac(a):
    if a == 0:
        return 1
    else:
        return a*fac(a-1)
a = int(input("Enter a number: "))
print(fac(a))'''

'''mystr = "python world"
for i in range(len(mystr)):
    print(i,mystr[i], end=" ")'''

'''def add(a,b):
    return a+b

def power(b,e):
    return b**e

print(add.__doc__)
print(power.__doc__)'''

# write a python program using function to convert celsius to fahrenheit.

'''def cel_to_feh(cel):
    feh = (cel * 9/5)+32
    print(feh)

cel = float(input("Enter the celsius: "))
cel_to_feh(cel)
'''

# write a program to convert inches into cms.

'''def inches_to_cm(In):
    cm = In*2.54
    print(cm)

In = float(input("Enter the inches: "))
inches_to_cm(In)'''

# 1. Write a Python function to find the maximum of three numbers.

'''def max_num(x,y,z):
    if x>y and x>z:
        print(x,"is the greatest number")
    elif y>x and y>z:
        print(y,"is the greatest number")
    else:
        print(z,"is the greatest number")

x = int(input("Enter the number 1: "))
y = int(input("Enter the number 2: "))
z = int(input("Enter the number 3: "))
max_num(x,y,z)'''

# 2. Write a Python function to sum all the numbers in a list.

'''def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return numbers
print(sum((2,3,4,5,6)))'''

# 3. Write a Python function to multiply all the numbers in a list.

'''def mul_list(numbers):
    mul = 1
    for x in numbers:
        mul = mul * x
    return mul
print(mul_list((2,3,4,1,2)))'''