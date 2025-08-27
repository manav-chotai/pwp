# a. Print all odd numbers between 1 and 100
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print("\n")

# b. Find the sum of all natural numbers between 1 to n
n = int(input("Enter a number for sum: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum of natural numbers from 1 to", n, "is:", total)
print("\n")

# c. Count number of digits in a number
def count_digits(num):
    count = 0
    if num == 0:
        return 1
    while num > 0:
        num //= 10
        count += 1
    return count

n = int(input("Enter a number to count digits: "))
print("Number of digits:", count_digits(n))
print("\n")

# d. Find the first and last digits of a number
n = int(input("Enter a number to find first and last digit: "))
last = n % 10
first = n
while first >= 10:
    first //= 10
print("First digit:", first)
print("Last digit:", last)
print("\n")

# e. Swap the first and last digits of a number
n = int(input("Enter a number to swap first and last digit: "))
num_str = str(n)
if len(num_str) == 1:
    swapped = num_str
else:
    swapped = num_str[-1] + num_str[1:-1] + num_str[0]
print("Number after swapping:", swapped)
print("\n")

# f. Calculate the product of digits of a number
n = int(input("Enter a number to find product of digits: "))
product = 1
temp = n
if n == 0:
    product = 0
else:
    while temp > 0:
        digit = temp % 10
        product *= digit
        temp //= 10
print("Product of digits:", product)
print("\n")

# g. Enter a number and print its reverse
n = int(input("Enter a number to reverse: "))
reverse = 0
temp = n
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("Reverse of", n, "is:", reverse)
