# def Keyword : creating a function in python a very specific syntax, including the def keyword, correct indentation and proper structure.

#def name_of_function() := Def Keyword  telling python this is  a function..

# def name_of_function(): defination of the functions.

'''def message():
    print("hello python")
message()
'''
# ADDITION OF TWO NUMBER USING FUNCTIONS.
'''def addition():
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))
    result = num1 + num2
    print("Addition of the given two number is : ",result)

addition()
addition()
addition()'''

#RETURN STATEMENT
'''def add(num1,num2):
    c = num1 + num2
    return c

num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))
sum = add(num1,num2)
print("The additon of the two given number is : ",sum)'''

'''sum = addition(12,23)
print(sum)'''
'''a = 89
b = 11
c = sum((a,b))  # It is a BUILT- IN FUNCTION.'''

'''def function():
     print("You are in function")
print(function())'''

'''def average(a , b):
     average = (a + b)/2
     #print(average)
     return average  #when you add this line then this not return None.

#print(average(23,45))  #It give you None.
avg = average(23,45)
print(avg)

def average(a , b):
     """This is a average which will calculate average of two numbers"""  # Docstring
     average = (a + b)/2
     #print(average)
     return average  #when you add this line then this not return None.

#print(average(23,45))  #It give you None.
#avg = average(23,45)
#print(avg)
print(average.__doc__)
'''
#******************************************************************************************

'''def addition(a,b,c):
     addition = a+b+c
     return addition

sum = addition(12,34,56)
print(sum)

def subtraction(a,b):
     subtraction = a-b
     return subtraction

sub = subtraction(12,4)
print(sub)

def multiplication(a,b):
     multiplication = a *b
     return multiplication

mul = multiplication(12,3)
print( mul)'''

'''def evenodd(a):
    if(a % 2 == 0):
        print(a,"is even number")
    else:
        print(a,"is odd number")
    return evenodd

result = evenodd(12)
print(result)'''

#*************************************************************************************************

#TRY AND EXCEPT EXCEPTIONAL HANDLING

'''num1 = input("Enter number 1 :")
num2 = input("Enter number 2 :")

try:
    print("The sum of these two number is : " ,int(num1) + int(num2))
except Exception as e:
    print(e)

print("This is very important")
'''

'''def say_hello():
    print("Hello")
    print("How")
    print("are")
    print("you ?")
print(say_hello())'''

'''def say_hello(name):
    print("Hello",name)  #0r print("Hello",{name})

print(say_hello('Sunny'))
'''
'''def add_num(num1, num2):
    return num1 + num2

sum = add_num(12,23)
print(sum)'''
'''def print_result(a,b):
    return a+b
sum = print_result(12,45)
print(sum)'''

'''def sum_num(num1 , num2):
    return num1 + num2

sum = sum_num(12,45)
print(sum)
'''
#*********************************************************************************************************

# FUNCTIONS WITH LOGICS.

'''def even_odd(num1):
    if(num1 % 2 == 0):
        print(num1,"is even")

    else:
        print(num1,"is odd")

even = even_odd(12)
print(even)'''

#OR

'''def even_check(number):
    result = number % 2 == 0
    return result

even = even_check(29)
print(even)'''

# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST.

'''def check_even_list(num_list):

    for number in num_list:
        if(number % 2 == 0):
            return True
        else:
            pass
    return False
even = check_even_list([1,3,5,7])
print(even)

even = check_even_list([2,6,4,8,10])
print(even)

even = check_even_list([12,34,23,35,56,67,89])
print(even)

even = check_even_list([11,34,23,35,56,67,89])
print(even)'''

# RETURN ALL THE EVEN NUMBER IN THE LIST.

'''def check_even_list(num_list):
    #return all the even number in the list.

    #  placeholder variables.
    even_numbers = []

    for number in num_list:
        if(number % 2 == 0):
            even_numbers.append(number)

        else:
            pass

    return even_numbers
even = check_even_list([1,3,5,7])
print(even)

even = check_even_list([2,6,4,8,10])
print(even)

even = check_even_list([12,34,23,35,56,67,89])
print(even)

even = check_even_list([11,34,23,35,56,67,89])
print(even)'''

# FUNCTION AND TUPLES  UNPACKING.

'''work_hours = [('Abby',100),('Billy',200),("Cassie",500)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

        else:
            pass

    return(employee_of_month,current_max)

result = employee_check(work_hours)
print(result)'''

#**********************************************************************************************
# INTERACTION BETWEEN PYTHON FUNCTIONS

'''example = [1,2,3,4,5,6,7,8]

from random import shuffle
result = shuffle(example)
print(result)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)

mylist = [" ", "o"," "]
shuffle_list(mylist)

def player_guess():
    guess = ' '
    while guess not in['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2")

    return int(guess)

print(player_guess())

def check_guess(mylist,guess):
    if mylist[guess] == 'o':
        print("Correct")

    else:
        print("Wrong guess")
        print(mylist)

# INITIAL LIST.
mylist = [' ','o',' ']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list,guess)'''

#**************************************************************************************************************

# *args and **kwargs

'''def percent(a,b):  # we can only take two argument.
    #  Return 5% of the sum of the number a and b
    return sum((a,b)) * 0.05

result  = percent(40,60)  # It is a positional argument coz 40 is assigned to a and 60 is assined to b.
print(result )'''

'''def percent(*args):  # args : arbitaray argument.
    # Through the help of args we can  take a multiple argument..
    return sum(args) * 0.05

result  = percent(40,60)
print(result)
result = percent(12,34,50,90,678)
print(result)'''

'''def percent(*args):  # args : arbitaray argument.
    for item in args:
        print(item)

percent(12,34,45,56,778,90)'''

# **kwargs : key  word arguments.

'''def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs :
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any food here")

myfunc(fruit='apple')
myfunc(fruit='banana')'''

'''def square(num):
    return num ** 2

my_list =  [1,2,3,4,5,6,7,8,9,10]
map(square,my_list)
list[(map(square,my_list))]
square(my_list)'''

'''def myfunc(*args):
    return sum(args)/10

result = myfunc(10,20,30,40)
print(result)'''


# print("" in "abc")


