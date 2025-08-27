# Q1: Convert degrees to radians
import math
deg = float(input("Enter degrees: "))
print("Radians:", math.radians(deg))

import math
# Q2: Calculate y = 6x^2 + 4sin(x)
x = float(input("Enter x: "))
y = 6*(x**2) + 4*math.sin(x)
print("y =", y)

import math
# Q3: f(x)=cos(2x), f'(x)=-2sin(2x), f''(x)=-4cos(2x), evaluate at x=π
x = math.pi
f = math.cos(2*x)
f1 = -2*math.sin(2*x)
f2 = -4*math.cos(2*x)
print("At x=π: f(x)=", f, ", f'(x)=", f1, ", f''(x)=", f2)
