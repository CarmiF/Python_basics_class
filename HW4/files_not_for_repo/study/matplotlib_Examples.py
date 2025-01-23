import numpy as np
import matplotlib.pyplot as plt

# Example 1
x = np.array ([1, 2, 3, 4, 5])
y = np.array ([50, 20, 30, 90, 100])
plt.plot (x,y)
plt.show()


# Example 1B
x = np.array ([1, 2, 3, 4, 5])
y = np.array ([50, 20, 30, 90, 100])
plt.plot (x,y, color = 'red', ls='--', marker ='o')
plt.xlabel('Bins')
plt.ylabel('Quantities')
plt.title('My Plot')
plt.show()

# Example 2
x = np.linspace(-np.pi, np.pi)
y, z = np.cos(x), np.sin(x)
plt.plot(x, y, color = 'green')
plt.plot(x, z, color = 'blue')
plt.show()

# Example 2B
x = np.linspace(-np.pi, np.pi)
y, z = np.cos(x), np.sin(x)
plt.plot(x, y, color = 'green')
plt.plot(x, z, color = 'r', ls='--')
plt.show()
