#  Operators

#  1. Arithmetic Operators

#  + ,-,*,/,% , ** (Power) , // (floor Division)

a = 5
b = 15

c = a ** b  # 5^15
print(c)

c = b // a  # o/p = 3
print(c)


# 2. Comparison Operators
# == , != , > , < , >= , <=

print(a != b)
print(a == b)
print(a >= b)
print(a < b)


#  3. Assignmant Operators
#  = , += ,-= , /= , %= , **= , //=
a += b
print(a)

a **= b
print(a)


# 4. Bitwise Operator
#  & , | , ^  , << , >> , ~

a = 401
b = 41
c = a | b
print(c)
c = a ^ b
print(c)
c = a & b << 1
print(c)
c = ~11
print(c)

# Logical Operator
#  and , or , not

print((a > 10 and b < 15))
print((a > 10 or b < 15))
print(not (a > 10 or b < 15))

# 5. Membership Operators
#  in , not in

print(a in range(0, 15))
print(a not in range(0, 15))

# 6. Identity Operators
#  is , is not

print(a is b)
print(a is not b)
