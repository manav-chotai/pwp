# a. Count the occurrences of an element in a tuple
t = (1, 2, 3, 2, 4, 2, 5)
print(t.count(2))

# b. Check if an element exists in a tuple
t = (1, 2, 3, 4, 5)
print(3 in t)

# c. Convert a tuple to a string
t = ('h', 'e', 'l', 'l', 'o')
print(''.join(t))

# d. Find the maximum and minimum elements in a tuple
t = (10, 25, 3, 45, 7)
print(max(t))
print(min(t))

# e. Convert a tuple of strings to a single string
t = ('Python', 'is', 'fun')
print(' '.join(t))

# f. Sort a tuple of integers
t = (5, 2, 8, 1, 9)
print(tuple(sorted(t)))

# g. Find the first and last elements of a tuple
t = (10, 20, 30, 40, 50)
print(t[0], t[-1])