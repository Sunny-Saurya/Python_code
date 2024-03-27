num = int(input("Enter number to check: "))
if num > 1:
    for i in range(2,num):
        if num % 2 == 0 or num % 3 == 0 or num % 7 == 0:
            print(num,"not a prime number")
            break
    else:
        print(num,"is prime number")
else:
    print(num,"is not a prime number")