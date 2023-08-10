# Any All in Python

# Any and All are two built-in functions provided in python used for successive And/Or. Any Returns true
# if any of the items is True. It returns False if empty or all are false. Any can be thought of as a
# sequence of OR operations on the provided iterables. It short circuit the execution i.e. stop the
# execution as soon as the result is known.

print(any([True, False, False, False, False]))
print(any([False, False, False, False, False]))
print(all([False, False, True, False, False]))
print(all([True, True, True, True, True]))
