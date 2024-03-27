#List Comprehesion :----> It is a easy and unique way of quickly creating a list with python.

'''my_strings = 'Sunny'
my_list = []
for letter in my_strings:
    my_list.append(letter)
print(my_list)'''

#OR

'''my_strings = 'Sunny'
my_list = [letter for letter in my_strings]
print(my_list)'''

'''my_list = [x for x in 'word']
print(my_list)'''

'''my_list = [qweqwe for qweqwe in 'wordtwo']
print(my_list)'''

'''my_list = [num for num in range(0,11)]
print(my_list)'''

#FOR SQUARE OF THE NUMBER.

'''my_list = [num**2 for num in range(0,11)]
print(my_list)'''

'''my_list = [alpha for alpha in "abcdef"]
print(my_list)'''

# We can also add condition in this loop..

'''my_list = [x for x in range(0,11) if x % 2 == 0]
print(my_list)'''

'''celcius = [0,10,20,30,32.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)'''

'''results = [x  if x % 2 == 0 else  'odd' for x in range(0,11)]
print(results)'''

'''my_list = []
for x in [2,4,6]:
    for  y in [1,10,1000]:
        my_list.append(x*y)
print(my_list)'''

# use a list comprehension and print all  the number which is divisible by 3 between 1 to 50.

'''my_list = [x for x in range(1 ,51)  if x % 3 == 0]
print(my_list)'''

'''name = "Sunnykumar"
print(name)
print(name[1:4])
print(name[1:9:1])'''

'''story = "Once upon a time "
print(len(story))
print(story.endswith(''time''))
print(story.count('o'))'''

'''name = input("Enter your name : ")
print("Good afternoon",name)'''


print([i for i in range(1,11)])
print([i*2 for i in range(1,11)])

x = [i*2 if i%2 == 0 else i*3 for i in range(1,11)]
print(x)

print([a for a in [1,2,3,4] for b in [2,4,5] if a == b])