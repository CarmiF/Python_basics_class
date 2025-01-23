# import numpy as np

# arr = np.array([[1,2,3],[1,2,3],[1,2,5]])
# print(arr.shape)
# print(arr.ndim)
# print
# print(arr)
# def rec(a,b):
#     if b==1: return a
#     # a=a+a
#     b=b-1
#     return rec(a,b)+a

# print(rec(3,5))

# def a(n,k,n1,k1):
#     s=0
#     if n==n1 and k==k1:
#         s=1
#     if k>n:
#         return s
#     elif k==0:
#         return s
#     else:
#         return a(n-1, k-1, n1,k1) + a(n-1,k,n1,k1)
    
# print(a(5,3,4,3))

# def list_sum(l):
#     if not l:
#         return 0
#     if isinstance(l[0], list):
#         l[0] = list_sum(l[0])

#     return list_sum(l[1:])+l[0]
    
# print(list_sum([1,2,3,[4,2,7],5]))

# arr = np.array([[30,31,29,30,31,32],[24,25,26,24,25,22],[34,34,34,35,36,36]])
# print(((arr > 0) & (arr < 60)).all())
# print( str(int(arr.argmax()/3)) + " "+ str(int(arr.argmax()/6))+" "+ str(arr.max()))
# print(arr[0:1:])
# print(arr)
# arr1 = sorted(np.argmax(arr, axis=0))[0]
# print(arr1)
# # unique, counts = np.unique(sorted(np.argmax(arr, axis=0), return_counts=))
# # print(unique)
# # print(counts)
# # print(np.argmax(counts))
# def local_maxima(arr):
#     arr = arr.reshape(arr.shape[1]/2, 2)
#     arr1 = arr

#     arr = arr.reshape(1, arr.shape[1]*2)
#     arr = np.where(arr==0)

# import numpy as np

# import numpy as np

# # Define the array
# arr = np.array([34, 1, 34, 35, 36, 36])

# # Ensure the array has at least 3 elements to have local maxima
# if len(arr) < 3:
#     print("Array does not have enough elements to have local maxima.")
# else:
#     # Identify local maxima (excluding the first and last elements)
#     local_maxima = (arr[1:-1] > arr[:-2]) & (arr[1:-1] > arr[2:])
    
#     # Adjust indices to match the original array
#     indices_of_local_maxima = np.where(local_maxima)[0] + 1
#     values_of_local_maxima = arr[indices_of_local_maxima]

#     print("Local maxima indices:", indices_of_local_maxima)
#     print("Local maxima values:", values_of_local_maxima)

import numpy as np

# Example 2D array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Normalize each row
print(A.max(axis=1)[:,np.newaxis])

A = A / A.max(axis=1)[:, np.newaxis]
print(A)
print([a for a in range(1,7,2)])