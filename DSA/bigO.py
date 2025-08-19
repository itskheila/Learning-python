#
#operations are the basic operations that are performed in a programor by a comp
#operations those that need to be added to each other


def calculate_sum(n):
    sum = 0
    for numb in range(n+1, 1):
        print (f"sum is {sum} and number is {numb}")
        sum= sum+numb
    print (f"for this {n} sum is {sum}")
    return sum # This code is for calculating the sum of numbers from 1 to n
    

def calculate_sum2(n):
    term1=n+1
    term2=n*term1
    sum=term2/2
    print(f"For {n} The sum is {sum}")
    return sum




import time
start_time = time.time()
calculate_sum(7777)
end_time= time.time()
diff=end_time-start_time
print(f"Speed{diff}")





#Big O notation

# Problem
# given a number calutate the total of sum
# 5-> 5+4+3+2+1
# 10-> 
import time

#sum=n(n+1)/2

#counting the number operations
# computer m=20,k=m*5

def calculate_sum(n):

    sum =0 #a
    for numb in range (1,n+1):#b,c
        print(f"sum ={sum} , numb={numb}")#d
        sum=sum+numb#e
    print(f"For {n} The sum is {sum}")#f
    return sum#g

def anotherfun():
    sum =0 #a
    for numb in range (1,n+1):#b,c
        print(f"sum ={sum} , numb={numb}")#d
        sum=sum+numb#e
    print(f"For {n} The sum is {sum}")#f
    return sum#g


    for numb in range(1,20):
        for k in range(3,40):
            print(numb)
            print(k)

#a+b+c(d+e)+g
# simplify =n
#n+n+n(n+n)+n
#3n(2n)+n
#6n^2+n
#n=1
#6+1
#10+2
#60000+100
# 6n^2-> 6(n^2)
# n^2->0(n)
def calculate_sum2(n):

    term1=n+1 #a
    term2=n*term1#b
    sum=term2/2#c
    print(f"For {n} The sum is {sum}")#d
    return sum#e

#a+b+c+d+e
#5n ->n
#O(1)


start_time=time.time()
calculate_sum2(200000)
end_time=time.time()
diff=end_time-start_time
print(f"Speed {diff}")