def z_transform_unit_step(z):
    return 1 / (1 - 1/z)
z = 2
print("Z-transform of unit step at z=2:", z_transform_unit_step(z))


import numpy as np
poles = np.array([0.6, 0.4])
if all(abs(p) < 1 for p in poles):
    print("System is: Stable")
else:
    print("System is: Unstable")
