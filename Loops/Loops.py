# for loop

for i in range(0, 10):
    print(i, end=" ")

print()

for i in range(10):
    print(i, end=" ")

print()

for i in range(0, 10, 3):
    print(i, end=" ")

print()


# while loop

i = 0
while i < 10:
    print(i, end=" @ ")
    i += 1


print()

i = 0
while i < 10:
    if i % 2 == 0:
        print(i, end=" ")
        i += 1
        continue
    elif i is 9:
        break
    else:
        i += 1


print()
