'''x = [1,3,5,3,"sunny"]
print(len(x))
'''
#list is ordered sequence of an element.

'''my_list = ['one','two']
print(my_list[0])'''

'''another_list = ["three","four"]
new_list = my_list + another_list
print(new_list)

new_list[1] = 'TWO IN CAPS'  #you can change it by using index number.
print(new_list)'''

#Additionn of a new elment into the list through append.

'''new_list.append('six')
print(new_list)

new_list.append("seven")
print(new_list)
'''
# Remove the last element  from the list through pop.

'''new_list.pop()
print(new_list)

popped_item = new_list.pop()
print(new_list)
print(popped_item)'''

# Remove the element from anywhere in the list. :- so we use index value.

'''counting = ['one','two','three']
counting.pop(0)
print(counting)

counting = ['one','two','three']
counting.pop(-1)
print(counting)'''

# Sorting of list in ordered.

'''sort = [1,4,63,6,34,6,9,7]
sort2 =  ['a','s','b','d','f']

sort.sort()
print(sort)

sort2.sort()
print(sort2)

sort.reverse()
print(sort)'''

#Practice  questions on list.

'''name = ['sunny','tannu','shubham','sagar']
print(name)
print(name[1])
print(name[1:])

name.append('isha')
print(name)

popped_value= name.pop(3)
print(name)
print(popped_value)

del name[2]
print(name)'''

'''list = [13,34,456,73,'sunny','tannu']
list.remove('sunny')
print(list)

del list[3]
print(list)'''

# list = [12,2,56,2,87,34,897]
# max = max(list)
# print(max)
# min = min(list)
# print(min)

# list  = [1,3,5,2,5]
# list_1 = [12,23,45,56]
# list_2 = [87,33,76]

# nested_list = [list,list_1,list_2]
# print(nested_list)

# print(nested_list[2])
# print(nested_list[0][0])
# print(nested_list[1][0])
# print(nested_list[2][2])
# print(nested_list[1][3])
# print(nested_list[0][4])

'''list1 = [1,2,3,4,5]
s = 0
i = 0
for i in list1:
    s = s + i
    i = i + 1
print(s)'''

'''list1 = [1,2,3,4,5]
m = 1
i = 0
for i in list1:
    m  = m * i
    i = i + 1
print(m)'''

# Write a Python program to get the largest number from a list.

'''list1 = [12,3,4,2,5]
max = list1[0]
for i in list1:
    if i > max:
        max = i
print(max)'''

#Write a Python program to get the largest number from a list. but take a list form the user.

'''number = int(input("Enter the number of digit: "))
list2 = []
for i in range(number):
    l1 = int(input("Enter your list: "))
    i = i+1
    print(l1)
    list2.append(l1)
print(list2)
max = list2[0]
for i in list2:
    if i>max:
        max = i
print("The max number in the given list is :",max)'''

# Write a Python program to get the smaller number from a list.

'''list1 = [100,2,3,4,5,6,7,8,9,10]
min = list1[0]
for i in list1:
    if i<min:
        min = i
print("The smaller number is :",min)'''

# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

str = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in str:
    if len(i) > 1 and i[0] == i[-1]:
        count = count+1
print(count)
        




    