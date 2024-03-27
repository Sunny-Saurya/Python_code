class Student:
    '''def __init__(self,name,age) -> None:
        self.name = name
        self.__age =  __age'''
    
    name = "python"
    __age = 23
    def getdata(self):
        print("Name: ",self.name)
        print("age: ",self.__age)

s1 = Student()
s1.getdata()