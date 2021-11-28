import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

x = np.linspace(0,1, 50)
y = (x * 2) + np.random.normal(0,2)
z = (y**2) - np.random.normal(2,10)

ax.scatter(x,y,z)
plt.show()