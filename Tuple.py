# tupleExs
# tupleExs is unchangeable (immutable)
# index start from 0
# Ordered
# Allow Duplicates

tupleEx = (1,2,3,4,5,6,7,"hello" ,1,2,3,4,5,"hi","hello")

print(len(tupleEx))
print(type(tupleEx))

for x in tupleEx:
    print(x,end=" ")

print()
# Slicing tupleExs in Python
print(tupleEx[:])    

print(tupleEx[1:5])
print(tupleEx[::-1])
print('>>>>>>>>><<<<<<<<<')
print(tupleEx[1:5:-1]) # o/p  is ()
print(tupleEx[1:len(tupleEx):2])

# tupleEx Constructor 
tupleEx1 = ("dsa", "developement", "deep learning")

print(tupleEx1)
print(type(tupleEx1) is tupleEx)
print(tupleEx1 is tupleEx)
print(tupleEx1 in tupleEx)


print(tupleEx[-len(tupleEx):-1])


# Code for concatenating 2 tupleExs

tupleEx2 = (0, 1, 2, 3)
tupleEx3 = ('python', 'geek')

tupleEx4 = tupleEx1 +tupleEx2 +tupleEx3

print(tupleEx4)
 
# Concatenating above two
print(tupleEx1 + tupleEx2)

# Nesting of Python tupleExs

tupleEx6 = (tupleEx1,tupleEx2)
print(tupleEx6)


# Repetition Python tupleExs

tupleEx7 = tupleEx6*4
print(tupleEx7)


# Converting a List to a tupleEx
list  = [1,2,3,4,5]
print(list)
print(tuple(list))

