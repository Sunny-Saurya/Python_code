#WHILE LOOP :
'''n = 1
while(n<=10):
    print("n is ", n)
    n += 1
print("these are the first 10 natural number")'''

# Print the sum of the first 10 natural number for both odd and even :

'''n = 1
sum = 0
while(n<=10):
    sum = sum + n
    n += 1
    print("The addition of the sum of the number 1 to 10 is : ", sum)'''

'''n = int(input("Enter the number"))
m = 1
sum = 0
while(m<=n):
    sum = sum + m
    m += 1
print("The addition of the sum of the number 1 to 10 is : ", sum)'''

# Only for odd :
'''
n = int(input("Enter the number"))
m = 1
sum = 0
while(m<=n):
    sum = sum + m
    m += 2
print("The addition of the sum of the number 1 to 10 is : ", sum)
'''

'''n = int(input("Enter the number"))
m = 1
sum = 0
while(m<=n):
    sum = sum + m
    m += 1
print("The addition of the sum of the number is : ", sum)
print("The addition of the sum of the neg. of the number is : ",-sum)'''

#Dictionary:

'''dict = {"Name": "Sunny Kumar", "Age":19,"Sex":"Male",
        "anotherdict": [1,2,4,5,6,8,98]}'''
'''print(dict['Name'])
print(dict['Age'])
print(dict['Sex'])
dict["anotherdict"] = [56,67,45] # it is mutable
print(dict["anotherdict"])''' # like this we can make a nested dictonary
# We cannot add the same key or value
'''print(dict.keys())
print(dict.values())
print(type(dict.keys()))
print(list(dict.keys()))
print(dict.items())'''
'''print(dict)
updatedict = {"Lovish": "Friend"}
dict.update(updatedict)
print(dict)
print(dict.get("anotherdict"))# it donot throws an error
print(dict["anotherdict2"]) #it throws an error'''

'''a = set()
print(type(a))
a.add(7)
a.add(4)
print(a)'''

'''mydict = {"bhulna":"forget","aana":"come","choro":"leave"}
print("options are :",(mydict.keys()))

a = input("Enter any hindi word : ")
#print("The english of the word that you are choosen is : ",mydict[a]) #if you print the word which is not in the option then it throws an error. if you want to get NONE instead of error then use GET() function.
print("The english of the word that you are choosen is : ", mydict.get(a))'''

'''a= 0xBee
b= 0o123456
print(a|b)'''
a = True
print(x>>a)