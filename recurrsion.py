# '''n =  int(input("Enter the number: "))
# a = 0
# for i in range(1,n):
#     if(n%i == 0):
#         a+=1
#     else:
#         pass
# if(a<=1):
#     print("prime")
# else:
#     print("not prime")'''
# k=1 
# for j in range(1,101):
#     for i in range(1,j):
#         if(j%i == 0):
#             k+=1
#             if(k<=1):
#                 print(j)
#             else:
#                 pass
#         else:
#             pass
#     if(k<=1):
#         print(j)
#     else:
#         pass

def fibo(idx):
    
    if idx<=1:
        return idx
    else:
        return fibo(idx-1)+fibo(idx-2)

print(fibo(8))

