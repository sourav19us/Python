#  List 
#  List are ordered
#  list is mutable type

# list_Name[Start:Stop:Step]

#  0, 1, 2, 3, 4, 5  <<<< index Value
# [1, 2, 3, 4, 5, 6]
# -6,-5,-4,-3,-2,-1  <<<< index Value

list1 = [] # empty list 

list1.append(1)
list1.append(2)
list1.append("Hey")
list1.append(14.35)

print(len(list1))
print(list1)

list1.insert(2,"Hi...")
print(len(list1))
print(list1)

list1.remove("Hey")
print(len(list1))
print(list1)


#  list constructor

list2 =  list((1 , 2 , 3 ,'hey'))
print(len(list2))
print(list2)

# extend()

list1.extend(list2)
print(len(list1))
print(list1)


list3 = list1.copy();
print(len(list3))
print(list3)

#  sort(reverse=True|False,key=myfun)

car = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print(car)

def myfun(e):
    return len(e)

car.sort(key=myfun)

print(car)
car.sort(reverse=True,key=myfun)

print(car)


print(list3[:])
print(list3[0:])
print(list3[2:5])
print(list3[-5:-1])
print(list3[2:len(list3):2])


print("hey" in list3)


n =  int(input("Enter the Num = "))
list14 = list(map(int,input("Enter element ").split()))[:n]
print(list14)



# list = list(map(int,input("Enter 10 Number").split()))

# i = 0
# print(type(list[0]))

# for x in list:
#     if(x > i):
#         i = x
        
# print("i = ",i)   

# for x in list:
#     for y in list:
#         if(y >= i):
#             print('*' ,end='')   
#         else:
#             print(' ',end='')
#     i-=1 
#     print()                 



# Method	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list    
    