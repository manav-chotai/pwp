# a. Display details of an image
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r"D:\ict\sem3\pwp\lecture code\labs\lab11\MU.jpg")
arr = np.array(img)
print("Dimensions:", arr.shape[0], "x", arr.shape[1])
print("Shape:", arr.shape)
print("Min value in Blue channel:", arr[:,:,2].min())

# b. Add black padding
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r"D:\ict\sem3\pwp\lecture code\labs\lab11\MU.jpg")
arr = np.array(img)

padded = np.zeros((arr.shape[0]+100, arr.shape[1]+100, 3), dtype=np.uint8)
padded[50:50+arr.shape[0], 50:50+arr.shape[1]] = arr

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(arr)
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(padded)
plt.title("Black Padded")
plt.axis("off")
plt.show()

# c. Show RGB channels
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r"D:\ict\sem3\pwp\lecture code\labs\lab11\MU.jpg")
arr = np.array(img)
R = arr[:,:,0]
G = arr[:,:,1]
B = arr[:,:,2]

plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.imshow(R, cmap="gray")
plt.title("Red Channel")
plt.axis("off")
plt.subplot(1,3,2)
plt.imshow(G, cmap="gray")
plt.title("Green Channel")
plt.axis("off")
plt.subplot(1,3,3)
plt.imshow(B, cmap="gray")
plt.title("Blue Channel")
plt.axis("off")
plt.show()
