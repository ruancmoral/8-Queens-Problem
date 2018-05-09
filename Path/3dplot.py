from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy
cost = 9
Points = 10
Cube_size = 10


fig = plt.figure(figsize=(10,8))
ax = Axes3D(fig)


x = numpy.random.randint(cost,size = Points)
y = numpy.random.randint(cost,size = Points)
z = numpy.random.randint(cost,size = Points)
line1 = ax.plot(x,y,z,'ok')
cont = 0
for x,y,z in zip(x,y,z):
    label = cont
    ax.text(x,y,z,label,color='red')
    cont+=1
#modify axes
ax.set_xlim(0,Cube_size)
ax.set_ylim(0,Cube_size)
ax.set_zlim(0,Cube_size)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.minorticks_on()
ax.tick_params(axis='both',which='minor',length=5,width=2,labelsize=18)
ax.tick_params(axis='both',which='major',length=8,width=2,labelsize=18)

#display 
plt.show()

