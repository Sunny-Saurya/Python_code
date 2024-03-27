# #method overloading is not possible in python;

# class Greeting:
#     def sayhello(self,name=None,add=None):
#         if name is not None and add is not None:
#             print("Hello"+name+add)
#         elif name is not None and add is None:
#             print("Hello"+name)
#         else:
#             print("None")
        
# c1= Greeting()
# c1.sayhello("Python","23")
# c1.sayhello("python")
# c1.sayhello()


'''class Car:
    def cardetails(self,color,brand):
        if color is not None and brand is None:
            print("Gwagon color is "+color)
        elif color is None and brand is not None:
            print("Gwagon brand is "+brand)
        elif color is not None and brand is not None:
            print("Gwagon color is "+color +"and brand is "+brand)
        else:
            print(None)
color = Car()
color.cardetails("black","benz")
color.cardetails("black")
color.cardetails("mercedez")'''

class Vehicle:
    def __init__(self, name):
        self.n = name
    
    def getdetails(self):
        print("name : ",self.n)

class bus(Vehicle):
    def __init__(self, model,color):
        self.model = model
        self.color = color
    
    def getbus(self):
        print("color: ",self.model)
        print("model: ",self.model)
b1 = bus("volvo","red")
b1.getbus()

