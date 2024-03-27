#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

'''num = 90
print(num+10.25)
print(num-(-10.25))
print(401/4)
print(10**2)'''

# What is the value of the expression 4 * (6 + 5)
print(4*(6+5)) #44

# What is the value of the expression 4 * 6 + 5
print(4*6+5) #29

# What is the value of the expression 4 + 6 * 5
print (4+6*5) #34

# What is the type of the result of the expression 3 + 1.5 + 4?

print(type(3+1.5+4))

# What would you use to find a number’s square root, as well as its square?

# FOR SQUARE ROOT :==> You have to do the power of 0.5 to  the given number ---> for eg.

num = 64
print(num**0.5)

# FOR SQUARE:===> You have to the power of 2 to the given number ----> for eg..

num = 8
print(num**2)

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

s = 'hello'
# Print out 'e' using indexing
print(s[1])

s ='hello'
# Reverse the string using slicing
print(s[::-1])

s ='hello'
# Print out the 'o'

# Method 1:
print(s[-1])

# Method 2:
print(s[4])

# Build this list [0,0,0] two separate ways.

# Method 1:
tup = (0,0,0)
print(list(tup))

# Method 2:
list = [0]
print(list*3)

# Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:

list4 = [5,3,4,6,1]
list4.sort()
print(list4)
#OR
print(sorted(list4))

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}

# Grab 'hello'

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}

# Grab 'hello'

print(d['k1']['k2'])

# Getting a little tricker

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello

'''print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!

d1 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d1['k1'][2]['k2'][1]['tough'][2][0])'''
# Can you sort a dictionary? Why or why not?

'''a = 1==2 and 3==3
print(a)

a = 1==2 or 3==3
print(a)

a = not(1==3)
print(a)'''