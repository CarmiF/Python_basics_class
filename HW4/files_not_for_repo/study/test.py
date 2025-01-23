import numpy as np

z = np.arange(1,10).reshape((3,3))
print(z)

print("~~~")
print(z[[1,2]][:,[1,2]])
# print(z)