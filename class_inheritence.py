class vehicle:
    def setdetails(self,name,model):
        self.n = name
        self.m = model
    def getdetails(self):
        print("Name :",self.n)
        print("Model: ",self.m)
    
class car(vehicle):
    def setcar(self,color):
        self.c = color
    def printcar(self):
        print("color: ",self.c)
    
n1 = input("enter name: ")
m1 = input("Enter the model name: ")
c1 = input("Enter the color: ")
v1 = vehicle()
car1 = car()
car1.setdetails(n1,m1)
car1.getdetails()
car1.setcar(c1)
car1.printcar()
v1.setdetails(n1,m1)
v1.getdetails()
