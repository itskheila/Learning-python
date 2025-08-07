#Args stands for arguments your function needs to take
#def stuff (name, gender, age)
#args will be a list of items being passed to the function
#*args is a way to pass a variable number of arguments to a function

def greet(*args):
    for value in args:
         print("Name is", value)

#greet("Jay","Mia","Mary", "Kile")

def sum(*args):
     ans=0
     for n in args:
          print(f"{ans}={ans}+{n}")
          ans=ans+n
          print("Answer is", ans)
          return ans
     
sum(1,2,3,4,5,100,543,1000)