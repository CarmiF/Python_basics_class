import numpy as np

# Define the lists
list1 = ['the', 'dog', 'alexa', 'sat', 'on', 'bob']
list2 = ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']

# Convert lists to numpy arrays
arr1 = np.array(list1)
arr2 = np.array(list2)

# Create a boolean mask where arr1 elements are found in arr2
mask = (arr1[:, np.newaxis] == arr2)

# Convert boolean mask to integers (1 for True, 0 for False)
result = mask.astype(int)

print(result)

