# Dictionary

# Dictionary in Python is a collection of keys values, used to store data values like a map, 
# which, unlike other data types which hold only a single value as an element.

# Note – Dictionary keys are case sensitive, the same name but different cases of Key will 
# be treated distinctly. 

Dict = {}
print(Dict)

# Adding elements one at a time
Dict[0] = 1
Dict[1] = 3
Dict[2] = 'hey'
Dict[3] = 'Hello'

print(Dict)

#  Updating existing Key's Value

Dict[0] = "One"
print(Dict)

# Accessing elements of a Dictionary
Dict[1] = {12:"h",145:"Joy"}
print(Dict)

# Accessing an element of a nested dictionary
Dict[1][12] = {1:"hi",2:"Joy",3:"Singh"}
print(Dict)

# Deleting Elements using del Keyword
del(Dict[3])
print(Dict)

# dict.keys()  = 	 Returns a list containing dictionary’s keys
print(Dict.keys())

for key in Dict.keys():
    print(Dict[key])

# dict.items()	 Returns a list containing a tuple for each key value pair

for key in Dict.keys():
    print(Dict.items())

for key , value in Dict.items():
    print("key = ",key,"value = ",value)


# Creating a Dictionary
# with dict() method

Dictex = dict({1:"One",2:"Two",3:"Three"})
print(Dictex)













