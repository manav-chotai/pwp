import sympy as sp
n, z = sp.symbols('n z')
x = 3**n
expr = x * z**(-n)
print("Z-transform of x[n] = 3^n u[n]:\n")
Xz_sum = sp.summation(expr, (n, 0, sp.oo))
sp.pprint(Xz_sum)
print("\nSimplified Form:")
sp.pprint(sp.simplify(Xz_sum))


import sympy as sp
n, z, w = sp.symbols('n z w')
x = sp.cos(w*n)
expr = x * z**(-n)
print("\n\nZ-transform of x[n] = cos(w n) u[n]:\n")
Xz_sum2 = sp.summation(expr, (n, 0, sp.oo))
sp.pprint(Xz_sum2)
print("\nSimplified Form:")
sp.pprint(sp.simplify(Xz_sum2))
