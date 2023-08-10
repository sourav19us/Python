# Sets in Python
# Set are represented by { }
# Check unique and  Immutable with Python Set
# Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered

set1 = {1,3,4}
print(type(set1))
print(set1)

# typecasting list to set
myset = set(["a", "b", "c"])
print(myset)


set2 = set()

for x in range(0,10):
    set2.add(x)

print(set2)



n = int(input('Enter n = '))
listEx = list(map(int,input("Enter Num ").split()))[:5]

set12 = set(listEx)

print(set12)

# Python Frozen Sets

# Frozen sets in Python are immutable objects that only support methods and operators that 
# produce a result without affecting the frozen set or sets to which they are applied. It can 
# be done with frozenset() method in Python.

# While elements of a set can be modified at any time, elements of the frozen set remain the 
# same after creation. 

frozensetEx = frozenset([1,2,4,5,"a","b"])
print(frozensetEx)





# Operators for Sets
# Sets and frozen sets support the following operators:

# Operators	          Notes
# key in s	          containment check
# key not in s	      non-containment check
# s1 == s2	          s1 is equivalent to s2
# s1 != s2	          s1 is not equivalent to s2
# s1 <= s2	          s1 is subset of s2
# s1 < s2	          s1 is proper subset of s2
# s1 >= s2	          s1 is superset of s2
# s1 > s2	          s1 is proper superset of s2
# s1 | s2	          the union of s1 and s2
# s1 & s2	          the intersection of s1 and s2
# s1 – s2	          the set of elements in s1 but not s2
# s1 ˆ s2	          the set of elements in precisely one of s1 or s2
