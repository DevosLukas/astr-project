# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 22:39:28 2018

@author: Iris
"""

#tijd x1 y1 z1 vx1 vy1 vz1 x2... xn yn zn vxn vyn vzn  
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

invoer = np.loadtxt("data.txt")
n = int((len(invoer[0])-1)/6) #aantal deeltjes

#omvormen naar lijst van deze vorm:
#[ [[x1,y1,z1][x2,y2,z2]...[xn,yn,zn]](t0)
#     [[x1,y1,y2][x2,y2,z2]...[xn,yn,zn]](t1)   ... (tn)]
punten = []
tijd = []
for lijn in invoer:
    tijd.append(lijn[0])
    deel = []
    for i in range(n):
        deel.append([lijn[1+i*6], lijn[2+i*6], lijn[3+i*6]])
    punten.append(deel)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
    
def update(p, *fargs):
    ax.set_title('t = {}'.format(round(tijd[p])))
    for i in range(n):
        ax.scatter3D(punten[p][i][0], punten[p][i][1], punten[p][i][2]) 

ani = animation.FuncAnimation(fig, update, frames = len(punten), fargs=(10,), interval = 100, blit = False)
ani.save('ani2.gif')