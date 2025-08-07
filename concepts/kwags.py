##Dictionary{key:vlue} kwags is a key looking at which value it is
# kwags,,,key word arguments
#a
def greet(name, nationality):
    print("Name is", name)
    print("from", nationality)
greet("Samson", "Babylon")
greet(nationality="Canada", name="Sam") # kwags is a key looking at which value it is
#kwags is working indirectly because its looking how to use the values

#KWARGS PROFILE
def employee(**kwargs):
    print(kwargs)

#{key:value}
employee(name="Samson",age=20,degree="Engineering")
employee(name="Samson",country="Kenya",degree="Engineering")