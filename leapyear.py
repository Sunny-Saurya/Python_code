'''year = int(input("Enter the number: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,"is a leap year")
else:
    print("not leap year")'''

'''n = int(input("Enter any number: "))
sum = 0
i = 1
while(n>0):
    sum = sum + n
    n = n+1
    i+=1
print(sum)

# Input: Get the value of n from the user
n = int(input("Enter a positive integer: "))

# Initialize a variable to store the sum
total = 0

# Loop from 1 to n and add each number to the sum
for i in range(1, n + 1):
    total += i

# Display the sum
print(f"The sum of the first {n} positive numbers is: {total}")'''


# Given a list, write a Python program to swap first and last element of the list.

'''list1 = [12,13,23,45,65]
l = len(list1)
temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp
print(list1)'''

# Find if an element exists in the list using a loop 

'''list1 = [1,2,3,4,5,6,7,8]
num = int(input("num too check: "))

if num in list1:
    print(True)
else:
    print(False)'''

'''list1 = [1,2,3,4,5,5]
list1.clear()
print(list1)'''

'''list1 = [1,2,3,4,5,6]
list2 = list1[:]
print(list2)

list3 = list1.copy()
print(list3)'''

list1= [1,2,3,2,1,2,2,2,4,5]
# num = int(input("num to check: "))
count = 0
for "2" in list1:
    count += 1
print(count)