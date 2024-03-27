'''a = input("Enter a number: ")
print(f"Multiplication of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("Invalid input")'''

#***************************** FINALLY *******************************

'''try:
    l = [1,2,3,4,5]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Invalid value")

finally:
    print("I am always be executed")'''

'''def Exception_handling(i):
    try:
        l = [1,2,3,4,5]
        print(l[i])
    except:
        print("Invalid value")

    finally:
        print("I am always be executed")
    
i = int(input("Enter the index: "))
Exception_handling(i)'''

#there are three tupe of error: syntax,logical, and runtime error.

'''a = 5
b = 0
try:
    print(a/b)
except:
    print("You cannot divide any number by zero")
print("Good Bye!")'''

'''a = 5
b = 0
try:
    print("open resoursse")
    print(a/b)
except Exception as e:
    print("You cannot divide any number by zero = ",e)
    print("close resouces")
print("Good Bye!") '''

# user defined error.

class Blanceexception(Exception):
    pass

'''def checkblance():
    money = 10000
    withdraw = 5000
    balance = money - withdraw
    print(balance)'''

try:
    money = 10000
    withdraw = 9000
    balance = money - withdraw
    if balance<=2000:
        raise Blanceexception("insufficient amount")
    print(balance)

except Blanceexception as e:
    print(e)
