import numpy as np


# A
def compute_distances(v, m):
    diff = m - v
    squared_diff = diff * diff
    squared_distances = np.sum(squared_diff, axis=1)
    return squared_distances


# B
def compute_distance_matrix(a, b):
    num_rows = a.shape[0]
    distances = np.zeros((num_rows, num_rows))
    for i in range(num_rows):
        distances[i] = compute_distances(a[i], b)
    return distances

