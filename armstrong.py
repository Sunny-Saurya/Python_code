num = int(input('Enter the three digit number to be checked for Armstrong: '))
t = num
cube_sum = 0

while t!= 0:
    k = t % 10
    cube_sum += k**3
    t = t//10
if cube_sum == num:
    print(num, ' is an Armstrong Number')
else:
    print(num, 'is not a Armstrong Number')

i = int(input("Enter number to check: "))
orig = i
sum = 0
while i>0:
    sum = sum + (i%10)*(i%10)*(i%10)
    i = i//10

if orig == sum:
    print("Number is Armstrong")
else:
    print("number is not armstrong")


def armstrong(n):
    orig = 0
    sum = 0
    while n>0:
        sum = sum+(n%10)*(n%10)*(n%10)
        n = n//10
    if orig == sum:
        print(n,"armstrong number")
    else:
        print(n,"not armstrong")

num = int(input("Enter the number: "))
armstrong(num)

dict1 = {1:'sunny',2: "vishal", 3:'rishav'}
for a,b in dict1.items():
    print(a,"is",b)