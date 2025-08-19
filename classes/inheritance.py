class Shape():
    def __init__(self,name):
        self.name = name

    def describe (self):
        print(f"This is a shape named {self.name}")

#shape1 = Shape(name="Star") 
#shape1.describe()

class Rectangle (Shape):
    def __init__(self,length,width):
        super().__init__("Rectangle")
        self.width=width
        self.height=length



r1 = Rectangle(length=5,width=10)
r1.describe()
print(f"the name of the shape is {r1.name}")
