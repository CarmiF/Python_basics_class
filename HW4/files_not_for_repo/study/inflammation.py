import numpy as np
fname = "inflammation-01.csv"
data = np.loadtxt(fname, delimiter=',')
print(data)
# properties of the data
print(type(data))
print(data.shape)
print("first value in data",data[0,0])


import matplotlib.pyplot as plt
plt.plot(data.mean(axis=0), label='avg')
plt.plot(data.max(axis=0), label='max')
plt.plot(data.min(axis=0), label='min')
plt.title('inflammation per day')
plt.legend()
plt.show()
