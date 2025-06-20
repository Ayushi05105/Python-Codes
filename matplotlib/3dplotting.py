from mpl_toolkits import mplot3d
import numpy as np



import matplotlib.pyplot as plt
fig = plt.figure(3)
ax = plt.axes(projection ='3d')
#plt.show()

z = np.linspace(0, 1, 100)
x= z * np.cos(25 * z)
y= z * np.sin(25 * z)
ax.plot3D(x, y, z, 'green')
#ax.set_title('3D Line Plot')
#plt.show()

c = x + y
ax.scatter(x,y,z,c=c)
ax.set_title('3D Scatter PLot')

plt.show()
