import numpy as np

# 1
b=np.array([[0, 1, 2], [3, 4, 5]])
print(b)
print(b.shape)

print(np.arange(6).reshape((2, 3)))

a = np.array([[0, 1, 2], [3, 4, 5]])

print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype.name)
print(a.itemsize)
print(type(a))


# 2
Z = np.random.random((5, 5))*99 + 1
print(Z)

z_min, z_max = Z.min(), Z.max()
print(z_min, z_max)


# 3
x = np.array([14, 22, 6, 30, 51, 44])
m = np.mean(x)
# var = np.mean((x-m)**2)
# print(var)
# print(np.var(x))


# # 4
# d = np.random.randint(-5, 6, (5, 5))
# print(d)
# print(d < 0)
# print(np.sum(d < 0, axis=0))


# # 5
# a = np.array([[1, 2], [3, 4]])
# b = np.array([10, 20, 30])
# # print(a + b)


# a = np.array([[1, 2], [3, 4]])
# c = np.array([[5, 10]])  # or np.array([5, 10])
# a += c
# print(a)


# 6
Z = np.zeros((8, 8), dtype=int)
Z[1::3, ::2] = 1
Z[::2, 1::2] = 1
print(Z)


# # 7
# A = np.array([3, 4, 6, 10, 24, 89, 45, 43, 46, 99, 100])
# print(A[A % 3 != 0])
# print(A[(A % 3 == 0) & (A % 5 == 0)])
# A[A % 3 == 0] = 42
# print(A)


# 8
nums = np.array([[3, 2, np.nan, 1], 
                 [10, 12, 10, 9], 
                 [5, np.nan, 1, np.nan]])
print("Original array:") 
print(nums) 
print("\nFind the missing data of the said array:") 
print(np.isnan(nums))
