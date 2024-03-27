#Map function.

'''def square(number):
    return number**2

my_number = [1,2,3,4,5]
for item in map(square,my_number):
    print(item)

result = list(map(square ,my_number))
print(result)'''

'''def splicer(mystrings):
    if len(mystrings) % 2 == 0:
        return "Even"
    else:
        return mystrings[0]

names = ['sunny','raju','andy']

result = list(map(splicer,names))
print(result)'''

# FILTER FUNCTION

'''def check_even(number):
    return number % 2 == 0

my_numbers =  [1,2,3,4,5,6]
result  = (filter(check_even,my_numbers))
print(list(result))

for n in filter(check_even,my_numbers):
    print(n)'''

# LAMBDA EXPRESSION.

# its normal function
'''def square(num):
    result = num ** 2
    return result
# its not lambda expressin 
result = square(2)
print(result)'''

# This is the lambda expression
'''square = lambda number : number ** 2
print(square(20))'''

# names =  ['Sunny', 'Andy', 'Sanju']
# reverse = list(map(lambda x:x[::-1],names))
# print(reverse)

a = "786"
a = int(a)
print(type(a))
print(a + 6)

