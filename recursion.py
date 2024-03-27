#Write the program to  find the factorial of a number by using recursion.

'''def fac_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fac_recursive(n-1)

number = int(input("Enter the number: "))
print(fac_recursive(number))'''

#Write the program to find the fibonacci series by using recursion method...

def fib_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
number = int(input("Enter the number: "))
print(fib_recursive(number))