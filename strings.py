# Slicing and Idexing of a strings.

'''mystring = "Sunnykumar"
print(mystring[-2])
print(mystring[:5])
print(mystring[:])
print(mystring[1:9:2])
print(mystring[::2])
print(mystring[::-1])'''

#IMMUTABILITY OF STRINGS :- THE THINGS THAT CAN NOT CHANGE.
#FOR EXAMPLE:

'''name = "Sam"
#print(name[0]) = 'p' #it can not be change.

print(name[1:])
last_latter = "am"
print('p'+'am')'''  # through this we can concatinate the strings.

'''x = "Hello World"
y = " It is very beautiful outside.\n"
print((x + y)*5) '''   # This is the process to change or concatinate the strings.

'''x = "Hello World"
print(x.capitalize())
print(x.isupper())
print(x.upper())
print(x.encode())
print(x.split("l"))
print(x.format())'''

# TO FIND ROOT OF ANY NUMBER JUST DO THE POWER OF 0.5.

'''a = 465**0.5
print(a)'''

'''name = "Sunny Kumar"
print(len(name))'''

'''a = "Hello World"
print(a[::-1])'''

'''a = "Hey everyone, I am Sunny: {}".format("I am 19")
print(a)'''

#THE DIFFERENT WAY TO CONCATINATE THE STRINGS :-- .format()

#print("This is string {}" .format("INSERTED"))

#print("This is a {} {} {} {} " .format('fox', 'black', 'flower' , 'sunny'))

#print("This is a {3} {0} {1} {2} " .format('fox', 'black', 'flower' , 'sunny'))

#print("This is a {3} {3} {3} {3} " .format('fox', 'black', 'flower' , 'sunny'))

#print("This is a {p} {s} {f} " .format(f = 'fox' , s = 'sunny' , p = 'flower'))

# FLOAT FORMATTING FOLLOWS { value:width.precision f }:

# result = 100/777

# print(result)

# print("The result was {r} " .format(r = result))

# print("The result was {r:10.3f} " .format(r = result))

# name = "Jose"
# print("Hello, his name is {}".format(name))

# print(f"Hello, his name is {name}")   # f string or formatting string literals.

# name = "Sunny"
# age = 19
# print(f'{name} is {age} years old')

# print("This is %s " %'sunny')

# print("This is %s ,He is %s"%('Sunny',19))

# print("This is %s ,He is %s, %s" %('Sunny',19, 'years old'))

#YOU CAN ALSO PASS VARIABLE NAMES.

# x,y,z = 'sunny', 19, 'years old'
# print("This is %s, he is %s, %s" %(x,y,z))

# print("This is %s" %("Sunny"))  #print without quotation mark.
# print("This is %r" %("Sunny"))  #print with quotation mark.

# print("I once caught a fish %s" % 'this \tbig')
# print("I once caught a fish %r" % 'this \tbig')

# print("I got %s in my test" % 10.55)
# print("I got %d in my test" % 10.55)

# print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
# print('{0:8} | {1:9}'.format('Apples', 3.))
# print('{0:8} | {1:9}'.format('Oranges', 10))

'''print("My name is %s" %("sunny"))
print("My name is %r" %('SUNNY'))
print("I got %s " %(89.34))
print("I got %d " %(89.34))

x = "sunny"
y = "paxton"

print("Hey everyone, This is %s" %('sunny'))

print("This is %s, I am %s %s" %('sunny',19,'years old'))

z = 'sunny'
a = 'paxton'

print("Hey, I am {} {}" .format(z,a))

x,y = 'sunny','paxton'
print("I am %s, My surname is %s" %(x,y))'''

'''print("Floating value is : %10.1f"  %(12.5343))
print("Floating value is : %20.1f"  %(12.5343))
print("Floating value is : %0.1f"  %(12.5343))

x  = 45.3425
print("Floating number is : %0.1f" %(x))
print("Floating number is : %1.1f" %(x))
print("Floating number is : %2.1f" %(x))
print("Floating number is : %3.1f" %(x))
print("Floating number is : %4.1f" %(x))
print("Floating number is : %5.1f" %(x))
print("Floating number is : %6.1f" %(x))'''

#MULTIPLE FORMATING

# print("I say My name is %s, my height is %2.2f, then okay %s" %('Sunny', 5.8889, 'bye!'))

#.formate()

'''print("This is {} {} {} {} ".format('fox','goat','ant','elephant'))
print("This is {3} {0} {2} {1} ".format('fox','goat','ant','elephant'))  #through indexing.


print('{0:8} | {1:9}'.format('Fruits', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 900))
print('{0:8} | {1:9}'.format('Oranges', 1000))'''

'''str = "    mygoodnessm     "
print(len(str))
print(str[:3])
print(str[::5])
print(str.endswith('god'))
print(str.endswith('o'))
print(str.count('o'))
print(str.capitalize())
print(str.find('g'))
print(str.replace("mygoodness","ohmygod"))
print(str.strip())'''

'''name=input("Enter your name: ")
print("Good morning",name)'''

'''str = "oh   my  goodness"
print(str.replace("   "," "))

str = "Dear Sunny\nThis python course is nice.\nThanks !"
print(str)'''

# fruits=["Apple","Oranges","Kiwi","Mango"]
# num=[23,12,56,34,90,32]
# print(fruits)
# print(fruits[2])
# print(fruits[0:3])
# print(fruits[1:3])
# print(num.reverse())

# n1 = 12
# n2 = 16
# n3 = 15
# n4 = 14
# n5 = 13
# list1 = []
# list1.append(n1)
# list1.append(n2)
# list1.append(n3)
# list1.append(n4)
# list1.append(n5)
# print(list1)

# list3 = []
# list4= (sum(list1))
# print(list4)

# list = [12,23,34,45,56]
# list.insert(3,45)
# print(list)
# list.pop(3)
# print(list)
# list.remove(45)
# print(list)

# n1 = 82
# n2 = 89
# n3 = 76
# n4 = 98
# n5 = 78
# list1 = []
# list1.append(n1)
# list1.append(n2)
# list1.append(n3)
# list1.append(n4)
# list1.append(n5)
# print(list1)
# print(sum(list1))

# dic = {'a':"apple", 'b':"banana",'c':"cat"}
# print(dic)
# dic.keys()
# print(dic)
# a = dic.update({"apple","Mango"})
# print(a)

# str = "my blog"
# a= ""
# for i in range(len(str)):
#     a = a + str[i]
# print(a)

'''str = "MyBlog"
a =""
for i in range(len(str)):
    print(i*str[i])'''

# for i in range(2,7,2):
#     print(i*"2")

# for i in range(3,12,2):
#     print("a".upper())

# for i in range(3,12,2):
#     print(i*"a".upper())

# str = "Welcome to my Blog"
# for i in str:
#     print(i)
# i = 0
# while(i<len(str)):
#     print(str[i])
#     i+=1

'''str = input("Enter  the strings: ")
n = 0
s = 0
for i in str:
    if i.isdigit() == True:
        n = int(i)
        s = s+n
print("the sum is :",s)'''

'''str = "python"
print(str[1:5])'''

str =  "string"
print(str.replace(str[0],str[-1]))
# print(str.replace(str[-1],str[0]))
# print(str[::-1])

import string
cap = string.ascii_uppercase
low= string.ascii_lowercase


