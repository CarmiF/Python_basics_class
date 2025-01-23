import numpy as np


# A
def align_matrices(M1, M2, L1, L2):
    perm = np.zeros(len(L1), dtype='int')
    for i in range(len(L1)):
        perm[i] = L2.index(L1[i])
    return M2[:, perm]


# B
def compute_consistency_measure(M1, M2, L1, L2):
    M2 = align_matrices(M1, M2, L1, L2)
    consistencyMat = ((M1 >= 60) & (M2 >= 60)) | ((M1 < 60) & (M2 < 60))
    return consistencyMat.sum(axis=0) / float(M1.shape[0])

