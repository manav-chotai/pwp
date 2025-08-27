# a. Create a 3x3 matrix with values ranging from 2 to 10
import numpy as np
a = np.arange(2, 11).reshape(3, 3)
print(a)

# b. Reverse an array
import numpy as np
b = np.array([1, 2, 3, 4, 5])
print(b[::-1])

# c. Find common values between two arrays
import numpy as np
c1 = np.array([1, 2, 3, 4])
c2 = np.array([3, 4, 5, 6])
print(np.intersect1d(c1, c2))

# d. Repeat array elements
import numpy as np
d = np.array([1, 2, 3])
print(np.repeat(d, 2))

# e. Find the memory size of a NumPy array
import numpy as np
e = np.array([10, 20, 30, 40, 50])
print(e.size * e.itemsize, "bytes")

# f. Create an array of ones and zeros
import numpy as np
f1 = np.ones((3, 3))
f2 = np.zeros((3, 3))
print(f1)
print(f2)

# g. Find the 4th element of a specified array
import numpy as np
g = np.array([10, 20, 30, 40, 50])
print(g[3])

