#  Python Literals
# 1. String Literals 

# single-line String

str = 'hi this is a Single-Line String'
print(str)

#  Multi Line String
str2 = 'hi this is \
        Multi Line String'
        
print(str2)

str3 = '''
          this is a
          Multi Line String
       '''

print(str3) 

#>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<
# 2. Numeric Literals  
x = 0b10101 # Binary Literals
y = 100 # Decimal Literals
z = 0o257 # Octal Literals
h =0x12d # Hexadecimal Literals
f = 100.56 # Float Literals
f2 =1.5e3  # Float Literals
f3 =1.5e-3  # Float Literals
c = 45.5+12.45j # Complex Literals

print(x) 
print(y) 
print(z) 
print(h) 
print(f) 
print(f2) 
print(f3) 
print(c) 


# >>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<

# 3. Boolean Literals
#  in this all  ex True = 1 and Fales = 0 
x = (1 == True) # 1 == 1 o/p is True
y = (4598 == False) # 4598 == 1 o/p is True
z = (48 == True) # 48== 1 o/p is True
h  = True + 12  # 1 + 12 o/p is 13
f  = False + 12 # 0 + 12 o/p is 12
print(x) 
print(y) 
print(z) 
print(h) 
print(f) 


# >>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<

# 4. Special Literals

n  =  None # The None keyword is used to define a null value, or no value at all
n2  = None
print(type(n))
print(n is n2) # True


