from tkinter import *
from PIL import Image, ImageTk

from math import *
from operator import truediv
import numpy as np
import matplotlib.pyplot as plt

from scipy import misc
import sys

## crÈation de l'objet fenÍtre
fenetre = Tk()

## sans le graphe
##Canvas(fenetre, width=480, height=320, bg='white').pack(side=LEFT, padx=5, pady=5)

## avec le graphe
"""
photo = PhotoImage("imageUS.png")
canvas = Canvas(fenetre,width=480,height=320) #premier test pour afficher le graphe
canvas.create_image(0,0,anchor=W,image=photo)
"""

## Frame2 pour les boutons

Frame2 = Frame(fenetre, borderwidth=2, relief = RIDGE)
Frame2.pack(side=RIGHT, padx=30, pady=30)


## label correspondant ‡ une fenetre avec son entrÈe qui reprÈsente les 5 paramËtres de la vue matriciel

def recupere():
    showinfo("Alerte",entree1.get(),entree2.gey(),entree3.get(),entree4.get(),entree5.get())

label1 = Label(Frame2, text="Position en x ")
label1.pack()
xRef = StringVar()
xRef.set("0")
entree1 = Entry(Frame2, textvariable=xRef, width=10)
entree1.pack()

label2 = Label(Frame2, text="Position en z ")
label2.pack()
zRef = StringVar()
zRef.set("0")
entree2 = Entry(Frame2, textvariable=zRef, width=10)
entree2.pack()

label3 = Label(Frame2, text="Ecart type en x")
label3.pack()
sigxRef = StringVar()
sigxRef.set("0")
entree3 = Entry(Frame2, textvariable=sigxRef, width=10)
entree3.pack()

label4 = Label(Frame2, text="Ecart type en z")
label4.pack()
sigzRef = StringVar()
sigzRef.set("0")
entree4 = Entry(Frame2, textvariable=sigzRef, width=10)
entree4.pack()

label5 = Label(Frame2, text="Amplitude ")
label5.pack()
ampRef = StringVar()
ampRef.set("0")
entree5 = Entry(Frame2, textvariable=ampRef, width=10)
entree5.pack()

##RÈcupËre les valeurs des 5 paramËtres
valeurs = Button(Frame2, text="RUN", command=recupere)
valeurs.pack()


def clavier(event):
    touche= event.keysys

    if valeurs == "Button-1":
        us_Matrice(entree1, entree2, entree3, entree4, entree5)
        image = Image.open("imageUS.png")
        photo = ImageTk.PhotoImage(image)

        ## Frame1 pour le graphe 
        Frame1 = Frame(fenetre, borderwidth=2, relief = GROOVE)
        Frame1.pack(side=LEFT, padx=30, pady=30)


        canvas = Canvas(Frame1,width=600,height=1000)
        canvas.bind("<Key>",clavier)
        canvas.create_image(400, 380, image=photo)
        canvas.pack(side=LEFT)

fenetre.mainloop()


def us_Matrice (xRef,zRef,sigxRef,sigzRef,ampRef):

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

