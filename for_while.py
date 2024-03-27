# Syntax of a for loop.

'''my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)'''

my_list = [1,2,3,4,5,6,7,8,9,10]

'''for item_name in my_list:
    print(item_name)
    print("Hello")'''

# Check even or odd.

'''for item_name in my_list:
    if(item_name % 2 == 0):
        print(item_name,"is even number")

    else:
        print(item_name,"is odd number")'''

# Sum of the first ten number.

'''list_sum = 0
for item_name in my_list:
    list_sum = list_sum + item_name
print(list_sum)'''

'''my_string = "Hello World"
for char in my_string:
    #print(char)
    print('cool!')'''

'''my_list = [(1,2),(3,4),(5,6),(7,8)]
print(len(my_list))'''

'''for item in my_list:
    print(item)'''

# If you want  To print Individual item of  the tuple then you can take a random tuple as name.

'''for (a,b) in  my_list:
    print(a)
    print(b)'''

'''dict = {'k1' : 1, 'k2': 2, 'k3' : 3}
#for i in dict:
    #print(i) # But by default it only print the key not print the values.

for value in dict.values():
    print(value)

for key in dict.keys():
    print(key)'''


#**************************************WHILE LOOPS ***********************************

#Syntax of a While loop
# While some_boolean_condition:
    #do something

#else:
    #do something different.

'''x = 0
while(x<5):
    print("The current value of x is",x)  # If we do not increment the value of x then it creat or print the INFINITE loop..
    x = x + 1

else:
    print("X is not less then 5")'''

# BREAK, CONTINUE, AND PASS

#BREAK: ---> Breaks out of the current closest enclosing loop

#CONTINUE ----> Continue goes to the top of the closest enclosing loop.

#PASS----> Does nothing at all..

'''mystring =  "Sammy"
for letter in mystring:
    if letter == 'm':
        break;
    print(letter)'''

'''mystring =  "Sammy"
for letter in mystring:
    if letter == 'm':
        continue;
    print(letter)'''

'''x = 0
while x<5:
    print(x)
    x += 1'''

'''for num in range(2,10,2):
    print(num)'''

'''index_count = 0
word = 'abcdef'

for letter in word:
    print(word[index_count])
    index_count += 1'''

# OR

'''ndex_count = 0

for letter in 'abcdef':
    print("At index {} the letter is {}" .format(index_count,letter))
    index_count += 1'''

# OR
# Enumerate  Function :---> it can take in any iterable object and it returns back some sort of index counter and then the object itself or the element.

word = 'abcdef'

'''for item in enumerate(word):
    print(item)'''

'''for index, letter in enumerate(word):  #so this is the enumerate function.
    print(index)
    print(letter)
    print('\n')
'''

# Zip function :----> it can pair the element as a tuples.

'''my_list = [1,2,3]
my_list1 = ['a','b','c']

for item in zip(my_list,my_list1):
    print(item)'''

'''my_list = [1,2,3,4,5,6]   # zip function ignores the element if anything is extra.
my_list2 = [100,200,300]
my_list1 = ['a','b','c']

for item in zip(my_list,my_list1,my_list2):
    print(item)'''

'''A = list(zip(my_list,my_list1,my_list2))
print(A)'''

# In operator :-->.if that element is  in the list then it returns true otherwise false.

'''x = [1,2,4,5,56]
print(5 in x)

print('a' in 'a world')

dict = {'mykey' : 345}
print(345 in dict.keys())
print('mykey' in dict.keys())'''

'''fav_num = int(input("Enter your favorite number"))
print(fav_num)
print(type(fav_num))'''

'''for num in range(0,101):
    if (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")
    elif (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    else:
        print(num)'''

# Go through the string below and if the length of a word is even print "even!"

'''st = 'Print every word in this sentence that has an even number of letters'
a = len(st)
if(a % 2 == 0):
    print("even")
else:

    print("odd")'''

# Use for, .split(), and if to create a Statement that will print out words that start with 's':

'''st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)'''

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
noah = [word[0] for word in st.split()]
print(noah)