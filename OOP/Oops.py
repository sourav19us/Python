# Python Classes and Objects

# Syntax: Class Definition

# class ClassName:
#     # Statement

# Syntax: Object Definition

# obj = ClassName()
# print(obj.atrr)

# Creating a Python Class 

class student:
    name = "Joy" # Static Variables
    # Self Parameter
    def fun(self): # at Name self you use Any Name
        print(f"Name is {self.name}")

    def funex2(instanceVar):
        print(instanceVar.name*3)
        
    def fullName(self,fName,lName):
        self.fName = fName  # Instance Variable
        self.lName = lName  # Instance Variable
        print(f" >>> {fName}   <<<< {lName}")
        print(f"First Name is {self.fName} and Last Name is {self.lName}")
    
    def allData(self):
        print(self.name ," " ,self.fName ,self.lName)   
        self.msg()  

    def msg(self):
        print("Hi Msg")
        
    # __init__() method
    # The __init__ method is similar to constructors in C++ and Java. 
    def __init__(self):
        print("This Is A Defult constructors")
        
    # >>>>>>>>> OR <<<<<<<<<< if use Both  then Error  only one constructors work
    # class only have one constructors if you write a more then one constructors then last one
    # is over write all constructors
    
    # def __init__(self,name):
    #     self.name = name
    #     print(f" Name is  {self.name}")        
    
    
        
# Creating Object 

obj = student()
obj.fun()
obj.funex2()
obj.name = "Jon"
obj.fun()
obj.funex2()

obj.fullName("Joy ", " Jon")
obj.fName = "Jjj"

obj.allData()

# Self Parameter
# When we call a method of this object as myobject.method(arg1, arg2), this is automatically 
# converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special 
# self is about. 

class student1:
    
    def __init__(self,Name):
        self.Name  = Name
        print(f" Name is {self.Name}")

obj2 =  student1("Joy @")

# __str__() method
# Python has a particular method called __str__(). that is used to define how a class object 
# should be represented as a string.

class studentEx12:
    def __init__(self , Name):
        self.Name = Name

    def __str__(self) -> str:
        return f"Name is {self.Name}"
    
    def show(self):
        print(f"Name is {self.Name}")

obj3 = studentEx12("Joy @#$")
print(obj3)

# Class and Instance Variables

obj3.Name ="Hii Joy"
obj3.show()



