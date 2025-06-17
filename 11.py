#import matplotlib.pyplot as plt
#%matplotlib inline  

class Circle:

    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

    def addRad(self,rad):
        self.radius = self.radius + rad

    """def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()"""

class Rectangle:

    def __init__(self,height,width,color):
        self.height = height
        self.width = width
        self.color = color

    """def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()"""

Circle1 = Circle(10,"Yellow")
rectangle1 = Rectangle(10,20,"Red")

Circle1.drawCircle()
rectangle1.drawRectangle()

class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def seatCap(self,seatCapacity):
        self.seatCapacity = seatCapacity

    def show(self):
        print(self.max_speed)
        print(self.mileage)
        print(self.seatCapacity)
        print(self.color)

car1 = Vehicle(200,20)
car2 = Vehicle(180,25)
car1.seatCap(5)
car2.seatCap(4)
car1.show()
car2.show()