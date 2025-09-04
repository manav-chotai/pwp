# a. Add, Subtract, Multiply and Divide two Pandas Series
import numpy as np
import pandas as pd
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([5, 10, 15, 20, 25])
print("Addition:\n", s1 + s2)
print("\nSubtraction:\n", s1 - s2)
print("\nMultiplication:\n", s1 * s2)
print("\nDivision:\n", s1 / s2)

# b. Convert a dictionary to a Pandas Series
import pandas as pd
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
series = pd.Series(data)
print(series)

# c. Create a series from a list, numpy array and dict
import pandas as pd
import numpy as np
list_data = [10, 20, 30, 40]
s_list = pd.Series(list_data)
print("Series from list:\n", s_list)

np_data = np.array([1, 2, 3, 4, 5])
s_np = pd.Series(np_data)
print("\nSeries from numpy array:\n", s_np)

dict_data = {'x': 100, 'y': 200, 'z': 300}
s_dict = pd.Series(dict_data)
print("\nSeries from dictionary:\n", s_dict)

# d. Stack two series vertically and horizontally
import pandas as pd
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])
vertical = pd.concat([s1, s2], axis=0)
print("Vertical Stack:\n", vertical)

horizontal = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:\n", horizontal)
