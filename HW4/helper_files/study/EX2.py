import numpy as np


def back_subst(R, b_tilde):
    n = R.shape[0]
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = b_tilde[i]
        for j in range(i+1, n):
            x[i] = x[i] - R[i, j]*x[j]
        x[i] = x[i]/R[i, i]
    return x
