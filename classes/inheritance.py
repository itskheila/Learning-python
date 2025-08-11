class Shape():
    def __init__(self,name):
        self.name = name

    def describe (self):
        print(f"This is a shape named {self.name}")

shape1 = Shape(name="Star") 
shape1.describe()