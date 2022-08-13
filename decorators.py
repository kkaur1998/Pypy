"""Decorator"""
"""Decorator: A Concept of Meta Programming. 
Decorator is used to update the functionality of a function.
Our today's target is how to create our own decorators
"""

# #New Program
# class C1:
#     @staticmethod
#     def func1():
#         print("I m in func1")

# #New Program
# def func1():
#     print("I am in func1")
# def func2():
#     print("I am in func2")

# print(func1)  #Say func1 address is 1000
# print(func2)    #Say func2 address is 2000
# m=func1     #func1 address is 1000
# n=func2     #func2 address is 2000    m and n will be called function pointer
# m()
# n()


# #New Program
# def func1():
#     print("I am in func1")
# def func2():
#     print("I am in func2")

# m=func1     #func1 address is 1000
# n=func2     #func2 address is 2000    m and n will be called function pointer
# m,n=n,m
# m()

# #New Program
# def func1():                    #func1 address 1000
#     print("I am in func1")
# def func2():                    #func2 address 2000
#     print("I am in func2")

# func1,func2=func2,func1         #func1 address 2000, #func2 address 1000
# func1()


"""How to call decorator using @function_name
Decorator is called immediately above function.
Decorator is also a function
Say we have one function as func1
"""
# #New Program
# def func1():                    #func1 address 1000
#     print("I am in func1")
#
#
# def func2():                    #func2 address 2000
#     print("I am in func2")
#
# func1,func2=func2,func1         #func1 address 2000, #func2 address 1000
# func1()

"""Delegation is representing a function through a variable"""
# # New Program
# def myDecorator(func):          #func is having address 1000 ie func1
#     def inner():       #Say inner address 2000
#         print("I am before func1 call")
#         func()      #Function of address 1000 called ie func1
#         print("I am After func1 call")
#     return inner

# @myDecorator                #func1=myDecorator(func1), now func1 address
#                             #will become 2000   #func1,func=inner,func1
# def func1():                #Say func1 address 1000
#     print("I am inside func1")

# func1()             #Now 2000 ie inner function will be called



# # New Program
# def myDecorator(func):          #func is having address 1000 ie func1
#     def inner():       #Say inner address 2000
#         print("I am before func call")
#         func()      #Function of address 1000 called ie func1
#         print("I am After func call")
#     return inner

# @myDecorator                #func1=myDecorator(func1), now func1 address
#                             #will become 2000   #func1,func=inner,func1
# def func1():                #Say func1 address 1000
#     print("I am inside func1")

# @myDecorator
# def func2():
#     print("I am in func2")

# func1()             #Now 2000 ie inner function will be called
# func2()


"""To create a time Decorator which always returns the time to execute
a function"""
import datetime
def timeDecorator(func):        #func address 1000, Say timeDecorator address 3000
    def inner(a):               #Say inner address is 2000
        t1=datetime.datetime.now()
        func(a)         #Now 1000 address function will be called
        t2=datetime.datetime.now()
        t=t2-t1
        print("Time to Execute Function:",t)
    return inner
@timeDecorator          #factorial=timeDecorator(factorial)
def factorial(a):       #factorial address 1000  after executing above statement factorial address 2000
    res=1
    for i in range(1,a+1):
        res=res*i
    print(f"Factorial of {a} is {res}")

factorial(1500)         #Here inner is called, inner(1500)


# #New Program
# import datetime
# def timeDecorator(func):        #func address 1000, Say timeDecorator address 3000
#     def inner(*t):               #Say inner address is 2000
#         t1=datetime.datetime.now()
#         func(*t)         #Now 1000 address function will be called
#         t2=datetime.datetime.now()
#         t=t2-t1
#         print("Time to Execute Function:",t)
#     return inner
# @timeDecorator          #factorial=timeDecorator(factorial)
# def factorial(a):       #factorial address 1000  after executing above statement factorial address 2000
#     res=1
#     for i in range(1,a+1):
#         res=res*i
#     print(f"Factorial of {a} is {res}")
#
# factorial(2000)         #Here inner is called, inner(1500)


# #New Program
# def func1(*t):          #Data is packed in t tuple using *t, actual
#     print(t)
#
#
# func1(2,3,4)            #Unpacked data at the time of calling, formal
# func1(5,6,7,8,9)

# # New Program
# def func1(a,b,c):  # Data is unpacked in three variables
#     print(a,b,c)
#
# t=(2,3,4)
# func1(*t)  # packed data at the time of calling, formal



# #New Program
# import datetime
# def timeDecorator(func):        #func address 1000, Say timeDecorator address 3000
#     def inner(*t):               #Say inner address is 2000
#         t1=datetime.datetime.now()
#         func(*t)         #Now 1000 address function will be called
#         t2=datetime.datetime.now()
#         t=t2-t1
#         print("Time to Execute Function:",t)
#     return inner
# @timeDecorator          #factorial=timeDecorator(factorial)
# def add(a,b,c):       #factorial address 1000  after executing above statement factorial address 2000
#     res=a+b+c
#     print(f"Addition of {a},{b},{c} is {res}")
#
# add(5,7,9)         #Here inner is called, inner(1500)


# #New Program
# import datetime
# def timeDecorator(func):        #func address 1000, Say timeDecorator address 3000
#     def inner(*t):               #Say inner address is 2000
#         t1=datetime.datetime.now()
#         result=func(*t)         #Now 1000 address function will be called
#         t2=datetime.datetime.now()
#         t=t2-t1
#         print("Time to Execute Function:",t)
#         return result
#     return inner
# @timeDecorator          #factorial=timeDecorator(factorial)
# def add(a,b,c):       #add address 1000  after executing above statement factorial address 2000
#     res=a+b+c
#     return res
#
# r=add(5,7,9)         #Here inner is called, inner(1500)
# print("Sum of Nos is:",r)


# #New Program
# import datetime
# def timeDecorator(func):        #func address 1000, Say timeDecorator address 3000
#     def inner(*t):               #Say inner address is 2000
#         t1=datetime.datetime.now()
#         result=func(*t)         #Now 1000 address function will be called
#         t2=datetime.datetime.now()
#         t=t2-t1
#         print("Time to Execute Function:",t)
#         return result
#     return inner
# @timeDecorator          #factorial=timeDecorator(factorial)
# def factorial(a):       #factorial address 1000  after executing above statement factorial address 2000
#     res=1
#     for i in range(1,a+1):
#         res=res*i
#     print(f"Factorial of {a} is {res}")
#
# factorial(2000)         #Here inner is called, inner(1500)


# #New Program
# import datetime
# def timeDecorator(func):        #func address 1000, Say timeDecorator address 3000
#     def inner(*t):               #Say inner address is 2000
#         t1=datetime.datetime.now()
#         result=func(*t)         #Now 1000 address function will be called
#         t2=datetime.datetime.now()
#         t=t2-t1
#         print("Time to Execute Function:",t)
#         return result
#     return inner
# @timeDecorator          #factorial=timeDecorator(factorial)
# def factorial(a):       #factorial address 1000  after executing above statement factorial address 2000
#     res=1
#     for i in range(1,a+1):
#         res=res*i
#     return res
#
# no=int(input("Enter Any No to calculate factorial:"))
# r=factorial(no)         #Here inner is called, inner(1500)
# print(f"Factorial of {no} is {r}")


# #New Program
# import datetime
# def timeDecorator(func):        #func address 1000, Say timeDecorator address 3000
#     def inner(*t):               #Say inner address is 2000
#         t1=datetime.datetime.now()
#         result=func(*t)         #Now 1000 address function will be called
#         t2=datetime.datetime.now()
#         t=t2-t1
#         print("Time to Execute Function:",t)
#         return result
#     return inner
# @timeDecorator          #factorial=timeDecorator(factorial)
# def func1():
#     L1=[]
#     for i in range(10000):
#         L1.append(i)
#     print(len(L1))
# func1()         #Here inner is called, inner(1500)


"""Create your own Library. Once you go for the interviews, discuss 
that you have your own library where you have created good no functions
which are not already available in Python"""

"""Last time I suggested to go for Competition websites."""

"""Last but not the least, once you become familiar with hackerrank and
hackerearth ie having some rank on these websites then final target is
Google official competition to crack: https://codingcompetitions.withgoogle.com/
Microsoft Official Competition: https://imaginecup.microsoft.com/en-us/Events?id=0
"""