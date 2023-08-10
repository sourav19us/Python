# input() => convert in  string

a = input("Enter a = ")
b = int(input("Enter a = "))
c = float(input("Enter a = "))
print(a, " ", b, " ", c, " ")

# if you enter more value then 3 then ValueError: too many values to unpack (expected 3)
a, b, c = input("enter 3 num ").split()
print(a, " ", b, " ", c, " ")

a, b, c = input("enter 3 num ").split(',')
print(a, " ", b, " ", c, " ")

a, b, c = input("enter a = "), input("enter b = "), input("enter c = ")
print(a, " ", b, " ", c, " ")


a, b, c = [int(x) for x in input().split()]  # convert str into int
print(a, " ", b, " ", c, " ")

# taking multiple input at a time

x = list(int(x) for x in input().split())
print(x)

x = list(map(int, input().split()))
print(x)


# output
print('Hello from ', end='@')
y = 15
z = 56
print(f" y = {y} , z = {z}", y, z)
print(" y = ", y, " ", "z = ", z)
print("y = {y} , z = {z}".format(y, z))
print("y =  %d and z = %d", y, z)
