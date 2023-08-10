 input from user
 a = int(input("Enter  a = "));
 b = int(input("Enter  b = "));
 print("a + b = ",(a+b));
a= 456
b=14
print("a + b = ",(a+b));

#  type()
c = 123.567
d = 'String'
e= 3+4j;
print(type(c)) # float
print(type(d))  # str
print(type(e)) # complex

# isinstance()
print(isinstance(c,float))
print(isinstance(c,str))
print(isinstance(d,str))
print(isinstance(e,complex))


# String

str = "Hello Joy ";
str2 = ">>>>>>>>>>>>>>>><<<<<<<<<<"
print(str[4])
print(str[:4])
print(str[2:6])
print(str+str2)
print(str*3)

# list

list = [14,"WDW",44,[4155,2536,425,41,455]]
list1 = [14,"WDW",44,425.36]
print(list) 
print(type(list))
# print(isinstance(list1,list))
print(list+list1)
print(list*2)
print(list[:1])
print(list[3][:3]) # index value start from 0 


# Tuple

tuple  = (1,"hi",'c++',41.25,(1,2,3,4))

print(tuple)
print(type(tuple))
print(tuple[:3])
print(tuple[:3:2])
print(tuple[4][:2])
print(tuple[4][:-2])

# Dictionary

Dictionary = {1:"hey",2:"L",'Hello':'Hellloooooo'}
print(type(Dictionary))
print(Dictionary[2])
print(Dictionary['Hello'])
print(Dictionary.keys()) #  give list of keys
print(Dictionary.values()) # give list of values

for i in Dictionary.keys():
    print('Key = ', i ,' And Value = ',Dictionary[i])
    
    
    
# set 
set1 = {1,2,3,1,5,4,7,7}    
print(set1) # {1, 2, 3, 4, 5, 7}
# print(set1[3]) # 'set' object is not subscriptable


# set2 = {1,2,5,3,{4,8,6,8,9}} # TypeError: unhashable type: 'set'
set2 = set(); # empty set()
print(set2)

# Boolean
b =True;
print(type(b))




