#initializer also a constructor
#initializer is the first method 
# that is called when an object is created
#each created method,,, must have the self keyword
#class,initializer,and keyword,self (need more content review on this)

class Human():

    def __init__(self,gender,name):
        print("Initializer is calledyy :)")
        
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

    def another_one(self):
        print("This is another method")


# adam.__init__()
#adam.__init__()
#adam.another_one()
adam=Human(name="adam",gender="Male") #object from a class
print("name",adam.name)
print("gender",adam.gender)
print("ribs",adam.ribs)
print("ribs",adam.curse)
print("")
eve=Human(name="eve",gender="Female")
print("name",eve.name)
print("gender",eve.gender)
print("ribs",eve.ribs)
print("curse",eve.curse)

