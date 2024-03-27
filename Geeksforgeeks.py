# 1. Python Program to Find the Factorial of a Number

'''import math  #by using maths module
n = int(input("Enter the number1: "))
print(math.factorial(n))'''

'''num = int(input("Enter the numebr you want to find the factorial of: "))

factorial = 1 

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
       print("The factorial of",num,"is",factorial)'''

# 2. Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

'''p = int(input("Enter your principal amount: "))
t = int(input("Enter time in year: "))
r = int(input("Enter the rate: "))
SI = (p*t*r)/100
print(SI)'''

#3. Let us discuss the formula for compound interest. The formula to calculate compound interest annually is given by: A = P(1 + R/100) t 

'''Compound Interest = A – P 

Where, 

A is amount 
P is the principal amount 
R is the rate and 
T is the time span'''     # 10000, 10.25, 5
'''
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter the  time: "))
Amount = principal * (pow((1 + rate / 100), time))
CI = Amount - principal
print("The compound interest is: ",CI)'''

#4. Write the program of armstrong number.

'''n = int(input("Enter the number to find the armstrong number : "))
orig = n
sum = 0
while n>0:
    sum = sum + (n%10)*(n%10)*(n%10)
    n = n//10

if orig == sum:
    print(n,"is the armstrong number")
else:
    print(n,"is not the armstrong number")'''

#5. Write the code to find the factorial of the given number.
'''
n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("The factorial of the given number is:",fact)'''

#6. Write the code where you take a list from the user and intercahnge the value of first and last element.

# lst = input("Enter the value:")
# list1=lst.split(",")
# print(list1)
# idx1 = int(input("Enter the first index value that you want to swap with: "))
# idx2 = int(input("Enter the second index value that you want to swap with: "))
# temp=list1[idx1]
# list1[idx1]=list1[idx2]
# list1[idx2]=temp
# print(list1)


'''lst = input("Enter the numebr: ")
list1 = lst.split(",")
print(list1)
idx1 = int(input("Enter the data: "))
idx2 = int(input("Enter the index2"))
temp = list1[idx1]
list1[idx1] = list1[idx2]
list1[idx2] = temp
print(list1)'''

'''list1 = [1,2,3,4,5,6]
list1.reverse()
print(list1)'''

#6. Python Program to Check if a String is Palindrome or Not

'''str = input("Enter your string: ")     #This is for palindrome string
orig = str  
if str[::-1] == orig:
    print(str,"yes this is palindrome string")
else:
    print("This is not palindrome string")'''

#This is for the palindrome digit

'''n =  int(input("Enter the number: "))
orig = n
s = 0
while(n>0):
    a=n%10
    s=s*10+a
    n=n//10

if(orig==s):
    print("palindrome")
else:
    print("not")'''

#7. Python program to check whether the string is Symmetrical or Palindrome
 
'''str = input("Enter the string: ")
orig = str
if str[::-1] == orig:
    print(str,"is palindrome")
else:
    print("This is not palidrome number")'''

#8. How to Remove Letters From a String in Python

'''str = "python"
print(str.replace('t',''))'''

# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.''')

'''list2 = [1,2,2,3,4,1,5,1,4,1,1,1]
num = int(input("num to check: "))
count = 0
for i in list2:
    if i == num:
        count+=1
print(count)'''

# list1 = [4,5,1,2,9,7,10,8]
# sum = 0
# for i in list1:
#     sum = sum + i
#     avg = sum/len(list1)
# print("sum is: ",sum)
# print("average is:",avg)

'''list1 = []
num = int(input("Enter the numbr you want ot print: "))

for i in range(1,num+1):
    ele = int(input("Enter element: "))
    list1.append(ele)
print("smallest element is:",min(list1))'''



# Python program to find second largest number in a list

'''list1 = [12,35,67,323,12,9]
list1.sort()
print(list1)
print("second largest no. is:",list1[-2])'''


'''data1 = input("data1: ")
data2 = input("data2: ")
list1 = data1.split(",")
list2 = data2.split(",")
print(list1)
print(list2)
result = sorted(dict.items())
print(result)'''

# list3 = 'hello'
# for i in list3:
#     i.split(",")
#     print(i,end=" ")

