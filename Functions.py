# Python Functions
# In Python a function is defined using the def keyword:

# syntax
#    
#    def function_name(parameters):
#          # statment
#          return expression

# Types of Functions in Python
# Built-in library function: These are Standard functions in Python that are available to use.
# User-defined function: We can create our own functions based on our requirements.

# Creating a Function in Python
def printMsg():
    print("Hello Joy")
    
    
# Calling a  Python Function
printMsg() 


# Function with Parameters
#  def function_name(parameter: data_type) -> return_type:
#     """Docstring"""
#     # body of the function
#     return expression

def sum(a,b):
    print(a+b)
    
sum(4,5)    
sum(4.55,5)    
# sum("hi",5)  error due to + operator work at same type data  
# sum(4,"Hello")    

def sumEx(a,b):
    print('a = ',a,'b = ',b)
    
sumEx("hi",5)  
sumEx(4,"Hello")    

def sumR(num1: int,num2: int) -> int:
    return num1 + num2

print(sumR(45,86))    
# print(sumR('hi',86))  only int parameters 
   
def sumRx(num1: str,num2: str):
    print(num1 + num2)
    print(f" num1 = {num1}  and num2  = {num2}")
    
print(sumRx('45','86'))  #  o/p is 4586 None for missing return type   
    
def sumRx(num1: str,num2: str):
    print(num1 + num2)
    return num1 + num2
print(sumRx('45','86'))  #  o/p is 4586 4586 for missing return type


# Types of Python Function Arguments   
# Default argument
# Keyword arguments (named arguments)
# Positional arguments
# Arbitrary arguments (variable-length arguments *args and **kwargs)

# Default argument

def addn( x , y=45):
    print(x+y)

addn(41)    
addn(41,450)    

# Keyword Arguments

def student(firstName,lastName):
    print(firstName,' ',lastName)
    print(firstName +' ' +lastName)
    
student(firstName='Joy',lastName="JOY")    

# Positional Arguments

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
    
nameAge('Joy',25)   
nameAge(25,'Joy')   

# Arbitrary Keyword  Arguments
# In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of 
# arguments to a function using special symbols. There are two special symbols:

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)


def myFun(*args):
    for a in args:
        print(a , end=" ")

myFun(1,2,3,4,5,6,7,8)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print()

def myFun2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        
myFun2(first='Geeks', mid='for', last='Geeks')        



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Docstring
# Syntax: print(function_name.__doc__)

def myFun3(x):
    """This is Doc For this function"""
    print(x)

print(myFun3.__doc__)    


# Python Function within Functions

def muFun4(x):
    
    print("x = ",x)
    
    def myFun():
        print("Hello from Within Function")
    
    myFun()


muFun4(45)        



# Anonymous Functions in Python
# In Python, an anonymous function means that a function is without a name. As we already know 
# the def keyword is used to define the normal functions and the lambda keyword is used to 
# create anonymous functions.

def sqr(x): return x**2

print(sqr(5))

sqr2 = lambda x : x**2

print(sqr2(45))


def swap(x, y):
    temp = x
    x = y
    y = temp
 
 
# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)