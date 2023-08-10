# Python Exception Handling


# Try and Except Statement – Catching Exceptions

a  = 5
try: # Some Code.... 
    print(a/0)
except ZeroDivisionError:
    print("You Try to divide by Zero")    
    
except:   # Catc All Exceptions
    print("a / 0")  

# Try with Else Clause
else: # execute if no exception
    print(f"a = {a}")
    
finally:  # Some code .....(always executed)
    print(f"a is {a}")
    
    
print("Hello From ")    

b = 6    
# except Exception as e:
try:
    print(b/0)
except Exception as e: # By this way we can know about the type of error occurring
    print('error is a ',e)    
    

# Raising Exception

# The raise statement allows the programmer to force a specific exception to occur. The sole 
# argument in raise indicates the exception to be raised. This must be either an exception 
# instance or an exception class (a class that derives from Exception).

try:
    if(a == 5):
        raise NameError(" This is A user defined Error") # Raise Error
except NameError:
    print("Error")
    raise  # To determine whether the exception was raised or not
    print("Error 11") # this line run due to raise
    
    

    
    
# SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, 
#               such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

# TypeError: This exception is raised when an operation or function is applied to an object of the
#               wrong type, such as adding a string to an integer.

# NameError: This exception is raised when a variable or function name is not found in the current scope.

# IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

# KeyError: This exception is raised when a key is not found in a dictionary.

# ValueError: This exception is raised when a function or method is called with an invalid argument 
#               or input, such as trying to convert a string to an integer when the string does not 
#               represent a valid integer.

# AttributeError: This exception is raised when an attribute or method is not found on an object,
#                   such as trying to access a non-existent attribute of a class instance.

# IOError: This exception is raised when an I/O operation, such as reading or writing a file, 
#           fails due to an input/output error.

# ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.

# ImportError: This exception is raised when an import statement fails to find or load a module.    