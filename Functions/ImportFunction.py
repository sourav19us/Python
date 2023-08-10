# Python  __import__() function

# import  the module at Run Time 

# Syntax: __import__(name, globals, locals, fromlist, level)

# Parameters:

# name: Name of the module to be imported

# globals and locals: Interpret names

# formlist: Objects or submodules to be imported (as a list)

# level: Specifies whether to use absolute or relative imports. The default is -1(absolute and relative).

# Exceptions of __import__ function in Python


# from numpy import complex as comp, array as arr
np = __import__('numpy', globals(), locals(), ['complex', 'array'], 0)
 
comp = np.complex
arr = np.array
 
comp_number = comp(5, 2)
my_arr = arr([1, 2, 3 , 4])
 
# prints the type
print(comp_number)
print(my_arr)