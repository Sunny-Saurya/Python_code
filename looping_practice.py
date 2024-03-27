#print all the number in list;
'''list = [1,2,3,4,5,6]
for i in list:
    print(i)'''

# Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

'''list = []
n = int(input("Enter number: "))
for i in range(1,n+1):
    num = int(input("Enter number: "))
    list.append(num)
print(list)
n = int(input("enter the number that you want to search: "))
if n in list:
    print(True,"this is in list")
else:
    print(False,"not in list")
'''

# Print multiplication table of 14 from a list in which multiplication table of 12 is stored.
'''a = 14
for i in range(1,13):
    print(a,"*",i,"=",a*i)
    i = i+1'''

# You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

'''list = []
n = int(input("Enter n: "))
for i in range(1,n+1):
    num = int(input("num: "))
    list.append(num)
print("The previous list without square",list)

list2 = []
for i in list:
    list1 = i**2
    list2.append(list1)
print("The list after squaring ",list2)'''

#Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.

'''list = []
list1  = []
for i in range(1,101):
    if i % 2 == 0:
        list.append(i)
    else:
        list1.append(i)
print("The list of even number is :",list)
print("The list of odd number is: ",list1)'''

# From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

'''list = []
list1  = []
list2 = []
for i in range(1,101):
    if i % 2 == 0:
        list.append(i)
    else:
        list1.append(i)
        
    if i % 4 == 0:
        list2.append(i)

print("The list of even number is :",list)
print("The list of odd number is: ",list1)
print("The list of digit divisible by 4:",list2)'''

# From a list containing ints, strings and floats, make three lists to store them separately.

ss = []
num=[]
fl = []
list = [12,"Ana","Sunny",56,98.8,"de","armas",45,9.55]
print(list)
for i in range(0,list):
    if list[i].isdigit()==True:
        num.append(list[i])

# Using range(1,101), make a list containing only prime numbers.

'''list =[]
for i in range(1,101):
    if i % 2 == 0 or i % 3 == 0 or i % 7 == 0:
        pass
    else:
        list.append(i)
list.append(2)
list.append(3)
list.append(7)
print(list)'''





