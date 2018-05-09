import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, PathPatch
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d

cmap = plt.get_cmap('spring') #define the colors of the plot 
colors = [cmap(i) for i in np.linspace(0.1, 0.9, n+1)]  

def cube(a,b,c,l): #plots a cube of side l at (a,b,c)  
        for ll in [0,l]:
            for i in range(3):
                dire= ["x","y","z"]
                xdire = [b,a,a] 
                ydire = [c,c,b]
                zdire = [a,b,c]
                side = Rectangle((xdire[i],                                                         ydire[i]),facecolors[np.where(sizes == l)[0]],edgecolor='black')
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=zdire[i]+ll, zdir=dire[i])

def plotter3D(X,Y,Z,sizes): #run cube(a,b,c,l) over the whole data set 
    for iX in range(len(X)):
        x = X[iX]
        y = Y[iX]
        z = Z[iX]
        for ix in range(len(x)): 
            cube(x[ix],y[ix],z[ix],sizes[iX])


fig = plt.figure() #open a figure 
ax=fig.gca(projection='3d') #make it 3d
plotter3D(X,Y,Z,sizes) #generate the cubes from the data set 
ax.set_xlim3d(0, length) #set the plot ranges 
ax.set_ylim3d(0, width)
ax.set_zlim3d(0, height)
plt.show()
