import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure("HERMIT")
ax = fig.add_subplot(111, projection = '3d')

T = np.array([[2,-2,1,1],[-3,3,-2,-1],[0,0,1,0],[1,0,0,0]])
P0 = [0,0,0]
P1 = [10,10,0]
d0 = 45
d1 = 45

D0 = math.tan((math.pi/180)*d0)
D1 = math.tan((math.pi/180)*d1)
print(D0 , D1)
Ax = np.array([[P0[0]],[P1[0]],[D0],[D1]])
Ay = np.array([[P0[1]],[P1[1]],[D0],[D1]])
Az = np.array([[P0[2]],[P1[2]],[D0],[D1]])

p_x = P0[0]
p_y = P0[1]
p_z = P0[2]
x= 0
y =0
z = 0

for i in range(0 , 101):
    u = i / 100
    U = np.array([[math.pow(u,3) , math.pow(u,2) ,u , 1]])
    x = U.dot(T.dot(Ax))
    y = U.dot(T.dot(Ay))
    z = U.dot(T.dot(Az))
    x = x[0][0]
    y = y[0][0]
    z = z[0][0]
    print(x)
    ax.plot([p_x , x],[p_y , y],[p_z , z])
    p_x = x
    p_y= y
    p_z = z
plt.xlabel("X_AXIS")
plt.ylabel("Y_AXIS")
plt.show()    
