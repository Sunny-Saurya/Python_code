'''#palindrome number:
num = input("Enter a number: ")
if num[0] == num[-1]:
    print("yes, this is palindrome number")
else:
    print("No, this is not palindrome number")'''

#armstrong
'''i = int(input("Enter any number: "))
orig = i
sum=0
while(i>0):
    sum = sum+(i%10)*(i%10)*(i%10)
    i = i//10
if orig == sum:
    print(sum,"is armstrong number")
else:
    print(sum, "is not armstrong numebr")'''

#gcd
'''num1 = int(input("enter any value:"))
num2 = int(input("enter any value:"))

if num1>num2:
    mn = num2
else:
    mn = num1

for i in range(1,mn+1):
    if num1%i == 0 and num2%i == 0:
        hcf = i
print(f"the hcf or gcd is {hcf}")'''

#fibonacci series

'''term = int(input("Enter the no. of terms: "))
a = 0
b = 1
sum = 0
for i in range(0,term):
    print(sum,end=" ")
    a = b
    b = sum
    sum = a+b'''
#program to check the leap year

'''year = int(input("enter the year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,"is the leap year")

else:
    print(year,"is not leap")'''

'''even
prime
armstrong
fibonacci
factorial
matrix
pascal'''

'''num = int(input("Enter number: "))
i = 1
while(num>1):
    for i in range(0,num+1):
        if'''

'''n=int(input())
i=1
list1= []
add=0
while i<n:
    for i in range(1,n+1):
        x=int(input())
        list1.append(x)
        add+=x
    i+=1
print(list1)
print(add)'''

'''r = float(input())
pi = 3.14
print("{0:.3f}".format(r*r*(pi)))'''

# uppercase to lower
#meters to kilometers upto 3 decimal places
#x ="python". Tke input from user eg. 2, print thonpy
# input an alphabet. Output should be the next alphabet.
# input n.take n integer input. create tuple with n and n**3
#farenheit to celcius
#append  a list in another list
#print abrakadabra.
#print cube root upto 3 decimal.
#print all prime numebr between n anad m:
#represent decimal numner in binary and octal.

#cel to feh
cel = float(input("Enter the temperature: "))
print("The feh of the given temperature is: ",9/5*cel + 32)

#feh to cel
feh = float(input("Enter the temp in fehreheite: "))
print("{0:.3f}".format(5/9*feh-32))