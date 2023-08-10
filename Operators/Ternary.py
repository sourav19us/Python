# Ternary Operator in Python

a, b = 10, 20

main = a if a < b else b

print(main)
main = a if a > b else b

print(main)


print(" a > b" if a > b else " b > a " if b > a else " a = b")


print(a, "a > b") if a > b else print(b, 'b <  a')


min = a < b and a or b

print(min)
