# -*- coding: Latin-1 -*- 
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


#Acoustic %
f0 = 5;                             # Central frequency (MHz)
c = 5;                             # Velocity (mm/us)
lamb = c/f0;                      # Wavelength (mm) 
dx = lamb/10;                    # x precision (mm)
dz = lamb/10;                     # z precision (mm)
#Imaging area %
xMin = 0;                         # x min (mm)
xMax = 40;                          # x max (mm)
zMin = 0;                           # z min (mm)
zMax = 45;                          #z max (mm)

#Reflectors %
xRef = np.array([10, 20,30]);                  # x position (mm)
zRef = np.array([15, 25, 35]);                  #z position (mm)
sigxRef =np.array( [0.5, 0.7, 0.9]);            #x standard deviation (mm)
sigzRef = np.array([0.6 ,0.8, 1]);              #z standard deviation (mm)
ampRef = np.array([1, 0.9 ,0.8]);               #Amplitude 



#Initializations %
x = np.arange(xMin,xMax,dx);
z = np.arange(zMin,zMax,dz);
Nx = len(x);
Nz = len(z);
Nref = len(xRef);
Y = np.zeros((Nz,Nx));

#Build the data with "Gaussian" model %
itref=np.array([1,2,1]);

#Y[itz,itx] = Y[itz,itx] + ampRef[itRef,]*exp(-1/(2*sigxRef[itRef,]^2)*
                        #(x[itx,]-xRef[itRef,]^2-1/(2*sigzRef[itRef,]^2)*(z[itz,]-zRef[itRef,]^2)

for itRef in range (0,Nref):
    for itx in range( 0,Nx):
        for itz in range(0,Nz):
            Y[itz,itx] = Y[itz,itx] + ampRef[itRef,]*exp(-1/(2*sigxRef[itRef,]**2)*
                        (x[itx,]-xRef[itRef,])**2 - 1/(2*sigzRef[itRef,]**2)*(z[itz,]-zRef[itRef,])**2)
    

 #Normalize image :max = 100 

Y_r= np.reshape(Y,(np.size(Y),1))
Y = 100*Y/max(abs(Y_r))


# Plot %


fig , (ax1)=plt.subplots( nrows=1 ,figsize=(6,6))
cbar=ax1.imshow(Y,extent=[xMin, xMax,zMax ,zMin], aspect='auto',cmap='jet')

#plt.gca().axis('equal')

fig.colorbar(cbar, ticks=[0,50, 100],orientation='vertical')
plt.ylabel('z(mm)')
plt.xlabel('x(mm)')
plt.title('synthetic data')
plt.savefig("imageUS.png")
plt.show()

plt.close()

'''
im=misc.imread('axe5essai.png',)


salt_value = 40

noise = np.random.randint(salt_value+1, im.shape)
indexe = np.where(noise == 0)

A = indexe[0]
B = indexe[1]

im[A,B,0] = 0.0
im[A,B,1] = 0.0
im[A,B,2] = 0.0

plt.show(im)'''
