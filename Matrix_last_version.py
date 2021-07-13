# -*- coding: Latin-1 -*-

#Library
from math import *
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as Tk
import sys
from time import time
import matplotlib.image as mpimg
from matplotlib.figure import Figure
from matplotlib import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Model():

    def __init__(self):

        #imaging area
        self.xMin = 0
        self.xMax = 40
        self.zMin = 0
        self.zMax = 45



        # Reflectors
        self.xRef = np.array([10, 20, 30])  # x position (mm)
        self.zRef = np.array([15, 25, 35])  # z position (mm)
        self.sigxRef = np.array([0.5, 0.7, 0.9])  # x standard deviation (mm)
        self.sigzRef = np.array([0.6, 0.8, 1])  # z standard deviation (mm)
        self.ampRef = np.array([1, 0.9, 0.8])  # Amplitude

    # Build the data with "Gaussian" model

    def gaussian(self,Nx,Nz):
        # Initializations
        self.x = np.linspace(self.xMin, self.xMax, Nx)
        self.z = np.linspace(self.zMin, self.zMax, Nz)
        self.Nref = len(self.xRef)
        self.DATA = np.zeros((Nz,Nx))

        for itRef in range(0,self.Nref):
            for itx in range(0,Nx):
                for itz in range(0,Nz):
                    self.DATA[itz, itx] = self.DATA[itz, itx] + self.ampRef[itRef,] * exp(
                        -1 / (2 * self.sigxRef[itRef,] ** 2) *
                        (self.x[itx,] - self.xRef[itRef,]) ** 2 - 1 / (2 * self.sigzRef[itRef,] ** 2) *
                        (self.z[itz,] - self.zRef[itRef,]) ** 2)
                    self.res = {"image": self.DATA}


    # Normalize image :max = 100
    def normalisation(self):
        self.DATA_r = np.reshape(self.DATA, (np.size(self.DATA), 1))
        self.DATA_norm = (100 * self.DATA) / max(abs(self.DATA_r))
        self.res2 = {"imagenorm": self.DATA_norm}



    # Creation of Gaussian noise

    def bruit(self,variance,Nx,Nz):

        bruit = np.random.randn(Nx,Nz) * variance #
        self.out = self.DATA_norm + bruit  # noisy picture
        self.res3 = {"imagebruit": self.out}

        #########################################################################

class SidePanel():
    def __init__(self, root):
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        self.runBut = Tk.Button(self.frame2, text="RUN ")
        self.runBut.pack(side="top", fill=Tk.BOTH)

        self.clearButton = Tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top", fill=Tk.BOTH)

        self.var1 = IntVar()
        self.var1.set(False)
        self.STOPBUT = Tk.Checkbutton(self.frame2, text="Stop", variable= self.var1)
        self.STOPBUT.pack(side="top", fill=Tk.BOTH)

        self.label1 = Label(self.frame2, text="Variance")
        self.label1.pack(side="top", fill=Tk.BOTH)
        variance = IntVar()
        variance.set(5)
        self.entree1 = Entry(self.frame2,textvariable=variance, width=10)
        self.entree1.pack(side="top", fill=Tk.BOTH)


        self.label7 = Label(self.frame2, text="Nx")
        self.label7.pack(side="top", fill=Tk.BOTH)
        valeur6 = IntVar()
        valeur6.set(512)
        self.entree7 = Entry(self.frame2, textvariable=valeur6, width=10)
        self.entree7.pack(side="top", fill=Tk.BOTH)

        self.label8 = Label(self.frame2, text="Nz")
        self.label8.pack(side="top", fill=Tk.BOTH)
        valeur7 = IntVar()
        valeur7.set(512)
        self.entree8 = Entry(self.frame2, textvariable=valeur7, width=10)
        self.entree8.pack(side="top", fill=Tk.BOTH)




class View():
    def __init__(self, master):
        self.frame1 = Tk.Frame(master)

        self.fig, self.ax0 = plt.subplots(nrows=1, figsize=(6,6), dpi=80)


        self.frame1.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel = SidePanel(master)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame1)

        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.show()


class Controller():

    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)

        self.view.sidepanel.runBut.bind("<Button>", self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>", self.clear)

        self.view.sidepanel.label1.bind("<Label>")
        self.view.sidepanel.entree1.bind("<Entry>")



    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()

    def clear(self, event):
        self.view.ax0.clear()
       # self.cb.remove()

        self.view.fig.canvas.draw()

    def my_plot(self, event):

        Nx = int(self.view.sidepanel.entree7.get())
        Nz = int(self.view.sidepanel.entree8.get())

        self.model.gaussian(Nx,Nz)
        self.model.normalisation()


        itFrame = 1
        fps_debut = time()
        while (self.view.sidepanel.var1.get()==0):
            plt.xlabel('x[mm]')
            plt.ylabel('z[mm]')

            self.model.bruit(int(self.view.sidepanel.entree1.get()),int(self.view.sidepanel.entree7.get()),
                                 int(self.view.sidepanel.entree8.get()))
            fps_fin = time()

            tframe=fps_fin-fps_debut
            self.FPS=itFrame / tframe
            itFrame = itFrame + 1

            #self.view.ax0.invert_yaxis()
            self.c = self.view.ax0.imshow(self.model.res3["imagebruit"], extent=[Model().xMin, Model().xMax, Model().zMax, Model().zMin]
                                            ,cmap='jet')


            self.label6 = Label(self.view.sidepanel.frame2, text="FPS ")
            self.label6.pack(side="top", fill=Tk.BOTH)
            self.label6.bind("<Label>")
            FPS_value = IntVar()
            FPS_value.set(round(self.FPS,2))
            self.entree6 = Entry(self.view.sidepanel.frame2, textvariable=FPS_value, width=10)
            self.entree6.pack(side="top", fill=Tk.BOTH)


            self.view.fig.canvas.draw()

            self.view.ax0.clear()

            self.label6.update()
            self.entree6.update()

            self.label6.destroy()
            self.entree6.destroy()

if __name__ == '__main__':
    c = Controller()
    c.run()
