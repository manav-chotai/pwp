# 1. Area and Perimeter of a Rectangle
length = float(input())
width = float(input())
area = length * width
perimeter = 2 * (length + width)
print(area)
print(perimeter)

# 2. Test if a number is even or odd
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Area and Volume of a Cube
side = float(input())
cube_area = 6 * (side ** 2)
cube_volume = side ** 3
print(cube_area)
print(cube_volume)

# 4. Solve z = (x+y)*(x-y)
x = float(input())
y = float(input())
z = (x + y) * (x - y)
print(z)

# 5. Solve z = (x+y)*(x+y)-2xy
x = float(input())
y = float(input())
z = (x + y) * (x + y) - 2 * x * y
print(z)

# 6. Convert Celsius to Fahrenheit
celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)
