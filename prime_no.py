'''n =  int(input("Enter the number: "))
a = 0
for i in range(1,n):
    if(n%i == 0):
        a+=1

    else:
        pass

if(a<=1):
    print("prime")
else:
    print("not prime")'''

# str = input("Enter the string: ")
'''if 'a' or 'A' in str:
    print(True)
else:
    print(False)'''

'''for i in range(1,11):
    if(i == 5):
        continue
    print(i)'''

'''for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i)'''

'''num = int(input("Enter the number: "))
for i in range(1,11):
    print(i,"*",num,"=",i*num)'''

'''list1 = int(input("Enter no. 1: "))
list2 = int(input("Enter no. 2: "))
list3 = int(input("Enter no. 3: "))
list4 = int(input("Enter no. 4: "))
list5 = int(input("Enter no. 5: "))
list6 = [list1,list2,list3,list4,list5]
for i in list6:
    if i % 2 == 0:
        print(i)
    else:
        pass'''

'''from math import gcd
def computeGCD(x,y):
    return gcd(x,y)
a = int(input("x: "))
b = int(input("y: "))
print(computeGCD(a,b))'''
    