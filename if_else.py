# Syntax of an if/else statement.

#if some condition:
    #excute some code

#elif:
    #do somthing different.

#else:
    #do something else

'''if 3>2:
    print("it is true")
'''
'''if 'Hungry' :
    print("Feed me !")
else:
    print("I am not hungry")'''

'''loc = 'Bank'

if loc == "Auto shop":
    print("cars are cool !")
else:
    print("I don't know much")'''

'''name = "Sammy"

if name == 'Frankie':
    print("Hello Frankie")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print("What is your name ?")'''

'''Age = int(input("Enter your age : "))
if Age >17:
    print("Congratulation, you are eligible to vote.")

else:
    print("Sorry, you are not eligible to vote.")'''

'''No_of_units = int(input("Enter the number of units : "))
amt = 0

if No_of_units <= 100:
    print("No charges",amt)

elif No_of_units > 100 and No_of_units <= 200:
    amt = (No_of_units -100)*5
    print(amt)

elif No_of_units > 200:
    amt =500+ (No_of_units - 200) * 10
    print(amt)'''

# a="Python"
# print(a[5:]+a[1:5]+a[0:1])

f = open("allah",'r')
content = f.read()
print(content)