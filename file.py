# f = open("data.txt","r")
# print(f.read())

#if you want to read the file then you have to mention that how much you want to read by passing some digit. or index number.

# f = open("data.txt","r")
# print(f.read(6))

# if you wnat ot add something or write something in your file then you have to write "w" rather than 'r'.

# f = open("data.txt","w")
# f.write("Ohhh! my goodness \n") 
# f.write("Hey bruhh ! I am Sunny")

#if you want to read and also want ot write then you have to write r + w emans in the file you can also write and read

# f = open("data.txt","r+w")
# f.write("Hello Everyone")

# f = open("text.txt","r+")
# print(f.read(5))
# f.write("hey buddy")

# f1 = open("Text.txt","w")
# data  = input("Enter text: ")
# f1.write(data)
# f1.close()
# f1 = open("Text.txt","r")
# print(f1.read(5))

# f = open("data2.txt","r+")
# print(f.readline())
# print(f.readline())
# print(f.readlines())


# f = open("data2.txt","a")
# f.write("hello")

# f = open("data2.txt","r+")
# f.seek(10)
# data = f.read(6)
# f2  = open("Text.txt","w")
# f2.write(data)

# REGULAR EXPRESSION.

# . ---> for any one character.
# for example: H.T = HOT,HIT,HAT,HITI,H@T...and so on.

# H[^a2@]t ---> this means expect this it could be aything.

#* --> 0 or more occurence of previous character. for example.

# Ha*t ---> ht,haat,haat,haaat,haaaat...and so on.

# if we club the two character then. H(at)* ---> Hatat, Hatatat,Hatatatat...and so one.

#(AB/CD)---> either ab or cd

# ^ab = all string beginnning with ab.
# $ab = dollar we can use for the ending.


# Ques. write an expression for finding a string which start with "a" and ends with "t".
 
# in this question we can use : ^a.*t$

# write an expression for email.  

# write an expression for phone number: 

''' [6-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9] or rather than writing it 9 times we can use.

[6-9][0-9]{9}'''

f = open("hello.txt",'r')
print(f)