# -*- coding: Latin-1 -*-

#Library
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from tkinter import *
import tkinter as Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Model():
 
    def __init__(self):

        #Acoustic
        
        self.f0=5                                  # Central frequency (MHz)
        self.c=5                                   # Velocity (mm/us)
        self.lamb = self.c/self.f0                 # Wavelength (mm)
        self.dx = self.lamb/10                     # x precision (mm)
        self.dz = self.lamb/10                     # z precision (mm)

        #Imaging area 
        self.xMin = 0                           # x min (mm)
        self.xMax = 40                          # x max (mm)
        self.zMin = 0                           # z min (mm)
        self.zMax = 45                          #z max (mm)
        self.res=None

        #Reflectors 
        self.xRef = np.array([10,20 ,30])                   # x position (mm)
        self.zRef = np.array([15 ,25, 35])                  #z position (mm)
        self.sigxRef = np.array( [0.5, 0.7, 0.9])           #x standard deviation (mm)
        self.sigzRef = np.array([0.6 ,0.8, 1])              #z standard deviation (mm)
        self.ampRef = np.array([1 ,0.9 ,0.8])               #Amplitude


        #Initializations 
        self.x = np.arange(self.xMin,self.xMax,self.dx)
        self.z = np.arange(self.zMin,self.zMax,self.dz)
        self.Nx = len(self.x)
        self.Nz = len(self.z)
        self.Nref = len(self.xRef)
        self.Y = np.zeros((self.Nz,self.Nx))
        self.Y_norm =np.zeros((self.Nz,self.Nx))
        self.variance=10
        
        #Build the data with "Gaussian" model

        
    def gaussian(self):
        for itRef in range(0,self.Nref):
            for itx in range(0,self.Nx):
                for itz in range(0,self.Nz):
                    self.Y[itz,itx] = self.Y[itz,itx] + self.ampRef[itRef,]*exp(-1/(2*self.sigxRef[itRef,]**2)*
                                (self.x[itx,]-self.xRef[itRef,])**2 - 1/(2*self.sigzRef[itRef,]**2)*
                                    (self.z[itz,]-self.zRef[itRef,])**2)
                    self.res= {"image":self.Y}
                    

        #Normalize image :max = 100
            
    def normalisation(self):    
        self.Y_r = np.reshape(self.Y,(np.size(self.Y),1))
        self.Y_norm = 100*self.Y/max(abs(self.Y_r))
        self.res2={"imagenorm":self.Y_norm}
    
    


        #Creation of Gaussian noise

    def bruit(self):

        ligne,colonne=(self.Y_norm).shape # Get the number of rows and columns
        
        bruit= np.random.randn(ligne,colonne)* self.variance# Gaussian noise : mean (0) and standard deviation (10)
        
        self.out=self.Y_norm+bruit; # noisy picture
        self.res3={"imagebruit":self.out}


    #########################################################################




class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.fig = Figure( figsize=(6,6))
        self.ax0=ax1.imshow(self.Y_norm,extent=[Model().xMin, Model().xMax, Model().zMax, Model().zMin], aspect='auto',cmap='jet')
        ## (10,10)(longueur,largeur) de la fenetre du graphe et dpi le nombre de pi
        self.ax0 = self.fig.add_axes( (0.02,0.02,0.80,0.80), axisbg=(0.75,0.75,0.75),
                                      frameon=False)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel=SidePanel(master)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.show()



class SidePanel():
    def __init__(self, root):
        self.frame2 = Tk.Frame( root )
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        
        self.runBut = Tk.Button(self.frame2, text="RUN ")
        self.runBut.pack(side="top",fill=Tk.BOTH)
        
        self.clearButton = Tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top",fill=Tk.BOTH)
        
        self.label1 = Label(self.frame2, text="Position en x ")
        self.label1.pack(side="top",fill=Tk.BOTH)
        self.entree1 = Entry(self.frame2, textvariable=StringVar(), width=10)
        self.entree1.pack(side="top",fill=Tk.BOTH)
        
        self.label2 = Label(self.frame2, text="Position en z ")
        self.label2.pack(side="top",fill=Tk.BOTH)
        self.entree2 = Entry(self.frame2, textvariable=StringVar(), width=10)
        self.entree2.pack(side="top",fill=Tk.BOTH)

        self.label3 = Label(self.frame2, text="écart type en x")
        self.label3.pack(side="top",fill=Tk.BOTH)
        self.entree3 = Entry(self.frame2, textvariable=StringVar(), width=10)
        self.entree3.pack(side="top",fill=Tk.BOTH)

        self.label4 = Label(self.frame2, text="écart type en z")
        self.label4.pack(side="top",fill=Tk.BOTH)
        self.entree4 = Entry(self.frame2, textvariable=StringVar(), width=10)
        self.entree4.pack(side="top",fill=Tk.BOTH)

        self.label5 = Label(self.frame2, text="Amplitude écho")
        self.label5.pack(side="top",fill=Tk.BOTH)
        self.entree5 = Entry(self.frame2, textvariable=StringVar(), width=10)
        self.entree5.pack(side="top",fill=Tk.BOTH)

       

        ####################################################################
class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model=Model()
        self.view=View(self.root)
        self.view.sidepanel.runBut.bind("<Button>",self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>",self.clear)
        
        self.view.sidepanel.label1.bind("<Label>")
        self.view.sidepanel.entree1.bind("<Entry>")
        
        self.view.sidepanel.label2.bind("<Label>")
        self.view.sidepanel.entree2.bind("<Entry>")
        
        self.view.sidepanel.label3.bind("<Label>")
        self.view.sidepanel.entree3.bind("<Entry>")
        
        self.view.sidepanel.label4.bind("<Label>")
        self.view.sidepanel.entree4.bind("<Entry>")
        
        self.view.sidepanel.label5.bind("<Label>")
        self.view.sidepanel.entree5.bind("<Entry>")
        
     

    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()
         
    def clear(self,event):
        self.view.ax0.clear()
        self.view.fig.canvas.draw()
  
    def my_plot(self,event):
        self.model.gaussian()
        #model.gaussian(Model().Y,Model().Nx,Model().Nz,Model().sigxRef,Model().sigzRef,Model().Nref,Model().ampRef,
                            #Model().xRef,Model().zRef,Model().x,Model().z)
        self.model.normalisation()
        self.model.bruit()
        self.view.ax0.clear()
        self.view.ax0.contourf(self.model.res3["imagebruit"])
        self.view.fig.canvas.draw()

if __name__ == '__main__':
    c = Controller()
    c.run()


