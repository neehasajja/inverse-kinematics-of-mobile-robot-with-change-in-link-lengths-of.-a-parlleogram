import numpy as np
import matplotlib as plt

plt.figue()
plt.ion()

#desired pose of the endeffector
P=np.array[1,1],[-1,-1]
R=np.array[1.0,0.0],[0.0,1.0] #2*2 of an identity matrix

#the vectors a,b a is from base frame to the arm
a1 =np.array[[0,0],[0,0]]
a2 =np.array[[0,0],[0,0]]

b1=np.array[[0.0],[0.0]]
b2=np.array[[0.0],[0.0]]

i=0
while i<50 :

#the solution
d1=p+np.dot(R,b1)-a1
d2=p+np.dot(R,b2)-a2

#extension of the length of the parallellogram/mobilerobot
length_d1=np.sqrt(d1[0]**2+d1[1]**2)
length_d2=np.sqrt(d2[0]**2+d2[1]**2)

print "length_d1 = ", Length_d1," length_d2= ",length_d2

plt.plot([a1[0],d1[0]+a1[0],p[0],d2[0],a2[0],a2[0]],a2[0],[a2[1],d1[1]])
plt.draw()
plt.pause(0.01)
i=i+1
p[0] = p[0]+0.04

plt.ioff()
plt.show()
