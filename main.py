#print("Hello World")
#Python is case sensitive language.

'''name = "Sunny"
age = 19
print(name)
print(age)

name = "Tannu"
print(name)

age = 19.23  #Boolean data type
print(age)

is_adult = True'''

'''name = (input("Enter your first name"))
age = 51
print(name,"is a genius")
print(name,"age is",age,"years old")'''

#If we want to take input from the user then the process is as follow.
'''name = input("Enter your name")
print(name)
print("Hello" + name)'''

'''shero = input("Who is your superhero?")
print(shero,"is my superhero")'''

#TYPE CONVERSION.

'''old_age = input("Enter your old age")
int(old_age)  #int is used for conversion the data type.
new_age = int(old_age) + 2
print(new_age)'''

#We can also convert float(), str(), char(),boolean().

'''num = 13
num2 =(float(13))
print(num2)'''

#Write a program of addition.

'''first = int(input("Enter first number"))
second = int(input("Enter second number"))
sum = first + second
print("The sum of the givne number is =",sum)'''

#Strings

'''name = "Sunny Kumar"
print(name.upper())
print(name.lower())
print(name)
print(name.find('S'))
print(name.find('r'))  #it  return a default value (-1).
print(name.find('Kumar'))

print(name.replace("Sunny Kumar", "Tannu Kumari")) #we can also replace the whole string.
print(name.replace('S','B'))'''  #with the help of this we can also replace the character.

#KEYWORDS.:- It is a reserved word which is used for a specific operation or task.

name = "Tannu Kumari"
print('T'in name)
print("iron man" in name)

#OPERATORS
#1. ARITHMATIC OPERATORS
'''print(5+8)
print(30-23)
print(34*2)
print(34/5)
print(100//5) #It return quotient.
print(100%5) #It gives the remainder
print(5**5)'''

i = 5
i = i + 4 # We can also write i+ = 4. It is basically a shorthand mathod in python.
print(i)

#OPERATOR PRECEDENCE IN PYTHON.

result = 2+4*5 #Multiplication has more precedence than addition.
print(result)

# #(COMMENT) IT IS A WELL MAINTAINER OF THE CODE. THIS IS CALLED A COMMENT. IF YOU WANT TO MAKE LINE COMMENT THAN BEFORE THAT CODE YOU CAN ADD HASHTAG#.

#COMPARISION OPERATOR. IT RETURN BOOLEAN VALUE(T/F)
print(2<6)
print(2>5)
print(2 == 2)
print(2 == 3)
print(2 != 3)

#LOGICAL OPERATOR. CONDITION BASED.
print(2>4 or 4<5)
print(3>2 and 2>4)
print(not 2 > 3) #not operator reverse the value or output or change the output.

#CONDITIONAL OPERATORS

'''age = 13
if(age >= 18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
print("Thank you. Namaskar")'''

'''age = int(input("Enter your actuall age"))

if(age >=21):
    print("You are eligible to marry")
elif(age<21):
    print("Go to school")
else:
    print("Just focus on study not on SHAADII")'''

#BUILT CALCULATOR BY USING PYTHON.

'''first = int(input("Enter first number"))
second = int(input("Enter second number"))
operator = input("enter the operator(+,-,*,/,%,//)")

if(operator == '+'):
    print(first + second)
elif(operator == '-'):
    print(first - second)
elif(operator == '*'):
    print(first * second)
elif(operator == '/'):
    print(first / second)
elif(operator == '%'):
    print(first % second)
elif(operator == '//'):
    print(first // second)
else:
    print("Invalid Operator")'''

#RANGE :- EK VALUE SE KISI OR VALUE ME JANA.

numbers = range(5)
print(numbers)

#LOOPS.
#WHILE LOOPS.

#PRINT THE FIRST TEN NATURAL NUMBER.

'''i = 1
while(i<=10):
    print(i)
    i = i + 1'''

#FOR PATTERN PRINTING.

'''i = 10
while(i>=1):
    print(i*"*")
    i = i - 1'''

'''i = 1
while(i<=10):
    print(i * "*")
    i = i + 1'''

#FOR LOOPS.

'''range(5)
for i in range(5000):
    print(i + 1)'''

#LISTS  IN PYTHON.:- LIST IS COLLECTION OF ITEMS.

'''marks = [54,34,123]   #it is a list.
print(marks)
print(marks[0])
print(marks[2])

print(marks[0:2])

for score in marks:
    print(score)

#APPEND.
marks.append(45)
print(marks)

#INSERT
marks.insert(0,87)
print(marks)

#keyword IN.
print(87 in marks)

print(len(marks))'''

#BY WHILE LOOP

'''i = 0
while(i<len(marks)):
    print(marks[i])
    i = i + 1'''

#BREAK AND CONTINUE.W

list = ["ram","radha","krishna","shyam","Lakshman"]

'''for student in list:
    if student == "krishna":
        break;
    print(student)

for student in list:
    if(student == "krishna"):
        continue;
    print(student)'''

#TUPLES.

'''marks = (98,76,53,32)
#marks[0] = 988    #TUPLE ARE IMMUTABLE, WE CAN CHANGE OR REPLACE THE VALUE IN TUPLES.
print(marks)
print(marks.index(32))

#SETS.

marks = {54,87,90,45,34,76,76,54} #IT ONLY RETURN UNIQUE VALUE NOT A DUPLICATE ONE.
print(marks)

for score in marks:
    print(score)'''

#DICTIONARY.:- key-value pair.

'''marks = {"english":76, "chemistry":87}
print(marks)
print(marks["chemistry"])

marks["physics"] = 100
print(marks)

marks["physics"] = 90
print(marks)'''

#WRITE A PROGRAM TO FIND THE TABLE OF  ANY NUMBER.

'''number = int(input("Enter any number to know the  table : "))
for n in range(1,11):
    print(number, '*', n, '=',number * n)'''


