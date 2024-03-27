# Funtion : function is used to reduce the length of the code.

'''def add():
    print("This is a function")
    print("End of the function")

print("BRfore calling function")
add()
print("After calling function")'''

#Write a program to gfind the additon of two number by usinf fucntion.
'''def add(a,b):
    c = a + b
    print("the addition of the given number is : ",c)
add(12,12)'''

# Addition program by using function and take input frokm the user.

'''a = int(input("Enter number a: "))
b  = int(input("Enter number b: "))
def add(a,b):
    sum = a+ b
    print("The sum of the given is: ",sum)
add(a,b)'''

'''a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
def add(a,b,c):
    sum = a+b+c
    print("sum is:",sum)
add(a,b,c)'''

# CALCULATOR BY USING FUNCTION:

'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter the operation you want to do(+,-,*,/,%,//): ")
if(op == '+'):
    def add(a,b):
        sum = a + b
        print("The sum of a and b is: ",sum)
    add(a,b)
elif (op == '-'):
        def sub (a, b):
            sub = a - b
            print("The sub of a and b is: ", sub)
        sub(a,b)
    
elif (op == '*'):
        def mul (a, b):
            mul = a * b
            print("The mul of a and b is: ", mul)
        mul(a, b)

elif (op == '+'):
        def div (a, b):
            div = a / b
            print("The div of a and b is: ", div)
        div(a, b)

elif (op == '%'):
        def mod (a, b):
            mod = a % b
            print("The mod of a and b is: ", mod)
        mod(a, b)
    
elif (op == '//'):
        def floor (a, b):
            floor = a // b
            print("The floor of a and b is: ", floor)
        floor(a, b)
else:
    print("please enter a valid number or operation")'''

'''def add(a,b):
    a = a+b
    print("a in additon",a)
a = int(input("a: "))
b = int(input("b: "))
print("a before add: ",a)
add(a,b)
print("a after add: ",a)
c = add(a,b)
print("c after add: ",c)'''

'''def sub(a,b):
    a = a-b
    print("subtraction of two given number is: ", a)
a = int(input("Enter a : "))
b = int(input("Enter b: "))
sub(a,b)'''

# Write a program to check wheather a number is even or odd
'''def even(a):
    if(a%2 == 0):
        print("Yes",a,"is even number")
    else:
        print(a ,"is odd number")

a = int(input("Enter a number a: "))
even(a)'''

'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter the operation you want to do(+,-,*,/,%,//): ")
if (op == '+'):
    def add(a, b):
        sum = a + b
        print("The sum of a and b is: ", sum)
    add(a, b)
elif (op == '-'):
    def sub(a, b):
        sub = a - b
        print("The sub of a and b is: ", sub)
    sub(a, b)

elif (op == '*'):
    def mul(a, b):
        mul = a * b
        print("The mul of a and b is: ", mul)
    mul(a, b)

elif (op == '+'):
    def div(a, b):
        div = a / b
        print("The div of a and b is: ", div)
    div(a, b)

elif (op == '%'):
    def mod(a, b):
        mod = a % b
        print("The mod of a and b is: ", mod)
    mod(a, b)

elif (op == '//'):
    def floor(a, b):
        floor = a // b
        print("The floor of a and b is: ", floor)
    floor(a, b)
else:
    print("please enter a valid number or operation")'''

'''def fib():
    n1 = int(input("Enter the number: "))
    a = 0
    b = 1
    sum = 0

    for i in range(0, n1):
        print(sum, end=" ")
        a = b
        b = sum
        sum = a + b
def fact():
    n2 =  int(input("enter the number to check the fact: "))
    fact = 1
    for i in range(1,n2+1):
        fact = fact*i
    print("The factorial of the ",n2, "is: ", end=" ")
    print(fact)

m = input("what do you want to check: fib or fact: ")
if m=='fib':
    fib()
else:
    fact()'''

#By default
'''def cal(a,b=10):
    print("addition: ",a+b)

a = int(input("Enter the fitrst numner: "))
b = int(input("Enter the second number:"))
cal(a,b)
cal(a)'''

#calculator by using fuction:

'''def add():
    a = int(input("Enter number a:"))
    b = int(input("enter number B:"))
    print("Addition of the given number is: ",a+b)
def sub():
    a = int(input("Enter number a:"))
    b = int(input("enter number B:"))
    print("Subtraction of the given number is:",a-b)
def mul():
    a = int(input("Enter number a:"))
    b = int(input("enter number B:"))
    print("multiplication of the given number is: ",a*b)
def div():
    a = int(input("Enter number a:"))
    b = int(input("enter number B:"))
    print("division of the given number:",a/b)

m = input("Enter the operator you want to do: ")

if m == "+":
    add()
elif m == "-":
    sub()
elif m == "*":
    mul()
elif m == "/":
    div()
else:
    print("Give a valid operator")'''

'''def cal(a,b=10):
    print("addition:",a+b)

def cal(a,b,c):
    print("a: ",a)
    print("b: ",b)
    #print("c: ",c)

n1 = int(input("Enter a number a: "))
n2 = int(input("Enter a number b: "))
n3 = int(input("Enter a number c: "))

cal(n1,n2,n3)'''

'''def fun1():
    global a
    a = 6

def fun2():
    a = 7

a = 5
print("a initially:",a)
fun1()
print("a after fun1:",a)
fun2()
print("a after fun2:",a)'''

'''def sub(a,b):
    print(a-b)
sub(3,2)
sub(a = 3, b = 2)
sub(b = 2, a = 3)
sub(4,5)'''

'''def welcome(msg, name):
    print(msg,name)'''

'''msg = input("Enter the massage: ")
name = input("Enter your name: ")'''
# welcome(msg,name)
# welcome(name = name,msg = msg)
# welcome(msg,name)
# welcome(name,msg)
# welcome(msg,name = name)
# welcome(msg=msg, name) # throws an error because you do not give the positional argument after keyword argument;
# welcome(name,msg= msg)  # throws an error because welcome() got multiple values for argument 'msg'


#WRITE A FUNCTION TO FIND THE GREATEST NUMBER OF THREE NUMBER;

'''def greatest(a,b,c):
    if a>b and a>c:
        print("The greatest number is",a)
    elif b>a and b>c:
        print("The greatest number is",b)
    else:
        print("The greatest number is",c)

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

greatest(a,b,c)
'''
#WRITE A PYTHON PROGRAM TO CONVERT THE CELSIUS INTO FEHRENHEIT.

'''def cel_feh(cel):
    print("The fehrenheit is:",(cel*9/5)+32)
cel = float(input("Enter the temperature: "))
cel_feh(cel)
'''

#WRITE A PROGRAM TO PRINT THE PATTER OF STAR BY USING FUCNTION.

def star(n):
    for i in range(n):
        print("*"*(n-i))
n = int(input("Enter the no. of rows: "))
star(n)