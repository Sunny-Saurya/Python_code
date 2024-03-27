
num = int(input("Enter the number: "))
a = 0
b =1
sum = 0

for i in range(0,num):
    print(sum,end=" ")
    a = b
    b = sum
    sum = a+b

num1 = int(input("n:"))
num2 = int(input("n: "))

if num1>num2:
    mn = num2
else:
    mn = num1

for i in range(1,mn+1):
    if num1%i == 0 and num2%i== 0:
        hcf = i
print(f"the hcf is {hcf}")

