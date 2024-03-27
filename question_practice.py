# num = input("Enter a list of number: ")
# list1 = list(num)
# tup = tuple(num)
# print(list1)
# print(tup)

# color_list = ["red","blue","yellow","green"]
# print(color_list[0])

# exam_date = input("Enter your exam date: ")
# exam_date = (12,23,2024)
# print("The examination date is %i / %i / %i" %exam_date)

#  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# n = int(input("Enter any number taht you want to evaluate: "))
# n1 = int("%s" %n)
# n2 = int("%s%s" %(n,n))
# n3 = int("%s%s%s" %(n,n,n))

# print(n1+n2+n3)

# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference

num = int(input("Enter any number: "))
n = 17
result = num-17
if(num>n):
    print(n*5)
else:
    print(abs(result))