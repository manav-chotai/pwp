# a. Multiply all the items in a list
numbers = [2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print(result)

# b. Get the largest number from a list
numbers = [10, 45, 32, 67, 89, 21]
print(max(numbers))

# c. Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
numbers = list(set(numbers))
print(numbers)

# d. Get the frequency of elements in a list
numbers = [1, 2, 2, 3, 4, 3, 3, 5]
freq = {}
for item in numbers:
    freq[item] = freq.get(item, 0) + 1
print(freq)

# e. Find common items from two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)

# f. Convert a list of multiple integers into a single integer
numbers = [1, 2, 3, 4, 5]
single_integer = int("".join(map(str, numbers)))
print(single_integer)
