'''letter = '''''' Dear <|NAME|>,
Greeting from ABC coding house. I am happy to tell you about your selection.
You are selected!

Date : <|DATE|>
''''''
name = input("Enter your name : ")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)'''

'''st = "Hello dear I am your   Sunny Kumar"
doubleSpaces = st.find("  ")
print(doubleSpaces) '''

'''st = "Hello dear I am your   Sunny Kumar"
doubleSpaces = st.replace("  ","")
print(doubleSpaces)'''

'''st = "Dear \n Harry, \n This python course is nice. \n Thanks "
print(st)'''

'''fruit1 = input("Enter the fruits no. 1")
fruit2 = input("Enter the fruits no. 2")
fruit3= input("Enter the fruits no. 3")
fruit4 = input("Enter the fruits no. 4")
fruit5 = input("Enter the fruits no. 5")
fruit6 = input("Enter the fruits no. 6")
fruit7 = input("Enter the fruits no. 7")

List = [fruit1, fruit2, fruit3,fruit4,fruit5,fruit6,fruit7]
print(List)'''

'''m1 = int(input("Enter the no. 1"))
m2 = int(input("Enter the no. 2"))
m3=  int(input("Enter the  no. 3"))
m4 = int(input("Enter the  no. 4"))
m5 = int(input("Enter the  no. 5"))
m6 = int(input("Enter the no. 6"))
m7 = int(input("Enter the  no. 7"))

my_list = [m1,m2,m3,m4,m5,m6,m7]
my_list.sort()
print(my_list)'''

'''num =float(input("enter the number you want to print : "))
print(num)
print(type(num))'''

'''num1 = int(input("Entet the number you want to print : "))
num2 = int(input("Entet the 2nd numebr oyou want to print : "))
total = num1 + num2
print("The addition of the two number is : ",total)'''

'''a = int(input("Enter the number : "))
b = int(input("Enter the 2nde numner : "))
avg = (a + b)/2
print(avg)'''

'''str = "Hello everyone, this is Sunny From New Delhi"
print(str)
print(len(str))
print(str.endswith("Delhi"))
print(str.count("i"))
print(str.capitalize())
print(str.find("this"))
print(str.replace("Sunny","Ayush"))'''

'''letter = """Dear </|NAME|>
You are selected ! 
<|DATE|>"""

name = input("Enter your name : ")
date = input("Enter date : ")

print(letter.replace("</|NAME|>",name))
print(letter.replace("<|DATE|>",date))'''

'''str = "Sunny  Kumar"
print(str)
print(str.find("  "))'''

'''a = 45
if(a>3):
    print("The calue of a is greater than 3")
else:
    print("The value of a is not greater tahn 3")'''

'''num1 = int(input("Enter the number 1: ") 
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))
num4 = int(input("Enter the number 4: "))

if num1>num2 and num1>num3 and num1>num4:
    print("The greatest no. is", num1)

elif num2>num1 and num2>num3 and num2>num4:
    print("The greatest no. is",num2)

elif num3>num1 and num3>num2 and num3>num4:
    print("The greatest no. is",num3)

else:
    print("The greatest no. is",num4)'''

#Write a program to print the number is prime or not.
'''num = int(input("Enter any number: "))
flag = 0
for i in range(2,num):
    if(num%i == 0 ):
        print(num,"is composite number")
        flag = 1
        break
if(flag == 0):
    print("Its a prime number ")'''

#WRITE A CODE TO PRINT THE ARMSTRONG NUMBER.

num = int(input('Enter the three digit number to be checked for Armstrong: '))
t = num
cube_sum = 0

while t!= 0:
    k = t % 10
    cube_sum += k**3
    t = t//10
if cube_sum == num:
    print(num, ' is an Armstrong Number')
else:
    print(num, 'is not a Armstrong Number')

'''num = int(input("Enter any number : "))
lenght = (len(num))
for i in range(0,lenght):'''
