# 1. is KeyWord
#  is (==) compare Two Object that Object is same Type or values

print(True is False) # False
print(True is True)  #  True
print(True is 'True') # False

# 2. in KeyWord
# The in keyword is used to check if a value is present in a sequence (list, range, string etc.).

# The in keyword is also used to iterate through a sequence in a for loop:

list = [1,2,3,"Hello","Hey"]
print(1 in list)
print('Hey' in list)
print('Hi' in list)

for i in list:
    print(i)
    
    
# pass Statement

# Definition and Usage
# The pass statement is used as a placeholder for future code.

# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
 
a = 14
b = 15
if a>b :
    pass
    print("hhhhhhh") # code line after pass not run 

for i in list:
    print("hhhhhhh") # code line before pass  run 
    pass


    