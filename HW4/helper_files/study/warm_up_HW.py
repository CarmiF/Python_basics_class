import numpy as np

# 1
x = np.ones((10, 10)) 
x[1:-1, 1:-1] = 0 
print(x)


# 2
Z = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print(Z)


# 3
x = np.eye(3) 
print(x)


