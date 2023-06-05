import math
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show


D = np.array([[-6.5,-6.5,-6.5,-6.5,-2.5,-2.5,-.75,-.75,3.25,3.25,4.5,4.5,6.5,6.5,6.5,6.5],
            [-2,-2,.5,.5,.5,.5,2,2,2,2,.5,.5,.5,.5,-2,-2],
            [-2.5,2.5,2.5,-2.5,-2.5,2.5,-2.5,2.5,-2.5,2.5,-2.5,2.5,-2.5,2.5,2.5,-2.5],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

C = np.array([[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]])

#perspective projection from center (-5,10,10)

P = np.array([[1,0,-.5,0],
            [0,1,-1,0],
            [0,0,0,0],
            [0,0,-.1,1]])
PD = np.matmul(P,D)
PD = PD/PD[3,:]
PD = np.delete(PD,-1,axis=0)

f, ax2 = plt.subplots(1)

for i in range(16):
    for j in range(i+1):
        if C[i,j]==1:
            ax2.plot([PD[0,i],PD[0,j]],[PD[1,i],PD[1,j]],'b')            

#perspective projection from center (0,10,25)

P = np.array([[1,0,0,0],
            [0,1,-.4,0],
            [0,0,0,0],
            [0,0,-.04,1]])

PD = np.matmul(P,D)
PD = PD/PD[3,:]
PD = np.delete(PD,-1,axis=0)

f, ax2 = plt.subplots(1)

for i in range(16):
    for j in range(i+1):
        if C[i,j]==1:
            ax2.plot([PD[0,i],PD[0,j]],[PD[1,i],PD[1,j]],'g')            

#rotation 30 degrees around y axis then perspective projection with center (0,10,25)
phi = math.pi/6
rotation_y = np.array([[math.cos(phi),0,math.sin(phi),0],
            [0,1,0,0],
            [-math.sin(phi),0,math.cos(phi),0],
            [0,0,0,1]])

P = np.array([[1,0,0,0],
            [0,1,-.4,0],
            [0,0,0,0],
            [0,0,-.04,1]])

RyD = np.matmul(rotation_y, D)
PRyD = np.matmul(P,RyD)
PRyD = PRyD/PRyD[3,:]
PRyD = np.delete(PRyD,-1,axis=0)

f, ax2 = plt.subplots(1)

for i in range(16):
    for j in range(i+1):
        if C[i,j]==1:
            ax2.plot([PRyD[0,i],PRyD[0,j]],[PRyD[1,i],PRyD[1,j]],'y')            

#rotation 45 degrees around z axis then perspective projection with center (0,10,25)

phi = math.pi/4
rotation_z = np.array([[math.cos(phi),-math.sin(phi),0,0],
            [math.sin(phi),math.cos(phi),0,0],
            [0,0,1,0],
            [0,0,0,1]])

P = np.array([[1,0,0,0],
            [0,1,-.4,0],
            [0,0,0,0],
            [0,0,-.04,1]])

RzD = np.matmul(rotation_z, D)
PRzD = np.matmul(P,RzD)
PRzD = PRzD/PRzD[3,:]
PRzD = np.delete(PRzD,-1,axis=0)

f, ax2 = plt.subplots(1)

for i in range(16):
    for j in range(i+1):
        if C[i,j]==1:
            ax2.plot([PRzD[0,i],PRzD[0,j]],[PRzD[1,i],PRzD[1,j]],'r')            

#scaling 150% then perspective projection with center (0,10,25)


scale = np.array([[1.5,0,0,0],
                [0,1.5,0,0],
                [0,0,1.5,0],
                [0,0,0,1]])

P = np.array([[1,0,0,0],
            [0,1,-.4,0],
            [0,0,0,0],
            [0,0,-.04,1]])

SD = np.matmul(scale, D)
PSD = np.matmul(P,SD)
PSD = PSD/PSD[3,:]
PSD = np.delete(PSD,-1,axis=0)

f, ax2 = plt.subplots(1)

for i in range(16):
    for j in range(i+1):
        if C[i,j]==1:
            ax2.plot([PSD[0,i],PSD[0,j]],[PSD[1,i],PSD[1,j]],'c')            

show()


