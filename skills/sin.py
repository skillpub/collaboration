'''sine graph'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2 * np.pi)
y = np.sin(x)

plt.stem(x, y)
plt.show()
