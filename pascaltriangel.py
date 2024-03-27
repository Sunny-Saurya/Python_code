# def pascal_triangle(row):
#     for i in range(0,row):  # to print the no. of rows
#         c = 1
#         for j in range(1,row-i):  # to print the space
#             print(" ",end=" ")
#         for k in range(0,i+1): #to print the line element
#             print(" ",c,end=" ")
#             c = c*(i-k)//(k+1)
#         print()
# n = int(input("Enter the number of  rows: "))
# pascal_triangle(n)


# class Parent:
#     def __init__(self,list1):
#         self.list1 = list1
#     def checklist(self):
#         l1 =[]
#         l2 = []
#         for i in self.list1:
#             if int(i) % 2 == 0:
#                 l1.append(int(i))
#             else:
#                 l2.append(int(i))
            
#         print(l1)
#         print(l2)
# list1 = input("enter the value:").split(",")
# p1 = Parent(list1)
# p1.checklist()


import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 50
h = 0

for i in range(400):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h = h + 1/n
    t.color(c)
    t.forward(i*2)
    t.left(145)

turtle.done()