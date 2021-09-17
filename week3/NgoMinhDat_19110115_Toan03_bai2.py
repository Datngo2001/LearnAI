
#this code reference from https://www.geeksforgeeks.org/numpy-meshgrid-function/

import numpy as np
from matplotlib import pyplot as plt
  
x = np.linspace(-100, 100, 101)
y = np.linspace(-100, 100, 101)

x, y = np.meshgrid(x, y)

z = x**3 + y**3

fig = plt.figure()
ax = fig.gca(projection = '3d')
mat_phang = ax.plot_surface(x,y,z)

plt.show()


