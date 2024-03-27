'''num = int(input("Enter the number of rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

'''z = input('Enter any char...: ')
if z == "a"  and "A" or z == "e" or z == "i" or z == "o" or  z == "u":
    print(z,"is a vowel")

else:
    print(z,"consonant")'''

'''i = int(input("x: "))
orig = i
sum = 0

while(i>0):
    sum = sum + (i%10)*(i%10)*(i%10)
    i = i // 10'''

num = int(input("Enter your number: "))
if num>1:
    for i in range(2,num):
        if(num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")

