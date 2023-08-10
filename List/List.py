# List
# Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and
# ArrayList in Java). In simple language, a list is a collection of things, enclosed in [ ] and separated
# by commas.

# The list is a sequence data type which is used to store the collection of data. Tuples and String are
# other types of sequence data types.

listb = []  # Blank List

list = list(map(int, input("Enter List Elements ").split()))

print(list)

list2 = [int(x) for x in input("Enter List Elements").split()]

print(list2)

for x in list2:
    print(list2[x], end=" ")
