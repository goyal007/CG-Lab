import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure("bezier curve")
ax = fig.add_subplot(111, projection = '3d' )
combination = []

N = 5   # N=control points
n = N-1 # n=order

def C(n,k):
    return( math.factorial(n)/(math.factorial(n-k) * math.factorial(k)))

for i in range(0,n+1):
    combination.append(C(n,i))
    
control_x = [0,10,20,10,0]
control_y = [0 , 10 , 0, -10,0]
control_z = [0 , 0, 0, 0,0]

for i in range(0,n):
    ax.plot([control_x[i], control_x[i+1]], [control_y[i], control_y[i+1]],[control_z[i], control_z[i+1]])
cprev_x = control_x[0]
cprev_y = control_y[0]
cprev_z = control_z[0]
for i in range(0 , 101):
    u = i/100
    x = 0
    y = 0
    z = 0
    for k in range(0 , n+1):
        blend = combination[k] * math.pow(u , k) * math.pow(1-u , n-k)
        x += control_x[k] * blend
        y += control_y[k] * blend
        z += control_z[k] * blend
    ax.plot([cprev_x , x] , [cprev_y, y] , [cprev_z , z])
    cprev_x = x
    cprev_y = y
    cprev_z = z
plt.xlabel("X_AXIS")
plt.ylabel("Y_AXIS")
plt.show()
