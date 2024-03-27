# Global and local variable:

'''def fun1():
    a = 5  # Local variable
    print("Value of a inside fun1: ",a)
a = int(input("enter a: "))   # Global variable
b = int(input("enter b: "))
fun1()
print("value of a after function call:",a)'''

'''def fun1():
    a = 5  # Local variable
    print("Value of a inside fun1: ",a)

def fun2(a):
    print("a times 2",a*2)

a = int(input("enter a: "))   # Global variable
print("Initial a :",a)
fun1(a)
print("value of a after function call:",a)
'''

def fun1(a):
    a = a+1
    print("a inside fun1:",a)
    return(a)

def fun2(a):
    print("a times 2: ",a*2)

a = int(input("Enter the a: "))
print("Initial a: ",a)
s = fun2(a)
print("value of a after function call: ",s)
