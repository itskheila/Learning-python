#helps extend or modify the behavior of 
#functions without changing their code

def my_deco(func):
    def wrapper():
        print("Before function run")
        func()
        print("Function completed running")
    return wrapper

@my_deco
def hello():
    print("hello world")

@my_deco
def greet ():
    print ("hello there")

hello()
greet()