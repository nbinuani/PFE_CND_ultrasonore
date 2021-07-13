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
from decimal import *
import matplotlib.pyplot as plt

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

        self.label1 = Label(self.frame2, text="Radius Min")
        self.label1.pack(side="top", fill=Tk.BOTH)
        valeur1 = IntVar()
        valeur1.set(0)
        self.entree1 = Entry(self.frame2, textvariable=valeur1, width=10)
        self.entree1.pack(side="top", fill=Tk.BOTH)

        self.label2 = Label(self.frame2, text="Radius Max")
        self.label2.pack(side="top", fill=Tk.BOTH)
        valeur2 = IntVar()
        valeur2.set(50)
        self.entree2 = Entry(self.frame2, textvariable=valeur2, width=10)
        self.entree2.pack(side="top", fill=Tk.BOTH)

        self.label3 = Label(self.frame2, text="Radius Step")
        self.label3.pack(side="top", fill=Tk.BOTH)
        valeur3 = DoubleVar()
        valeur3.set(0.01)
        self.entree3 = Entry(self.frame2, textvariable=valeur3, width=10)
        self.entree3.pack(side="top", fill=Tk.BOTH)

        self.label4 = Label(self.frame2, text="Angle Min")
        self.label4.pack(side="top", fill=Tk.BOTH)
        valeur4 = IntVar()
        valeur4.set(-45)
        self.entree4 = Entry(self.frame2, textvariable=valeur4, width=10)
        self.entree4.pack(side="top", fill=Tk.BOTH)

        self.label5 = Label(self.frame2, text="Angle Max")
        self.label5.pack(side="top", fill=Tk.BOTH)
        valeur5 = IntVar()
        valeur5.set(45)
        self.entree5 = Entry(self.frame2, textvariable=valeur5, width=10)
        self.entree5.pack(side="top", fill=Tk.BOTH)

        self.label6 = Label(self.frame2, text="Angle Step")
        self.label6.pack(side="top", fill=Tk.BOTH)
        valeur6 = IntVar()
        valeur6.set(1)
        self.entree6 = Entry(self.frame2, textvariable=valeur6, width=10)
        self.entree6.pack(side="top", fill=Tk.BOTH)

class View():
    def __init__(self, master):
        self.frame1 = Tk.Frame(master)

        self.fig, self.ax0 = plt.subplots(nrows=1, figsize=(6, 6), dpi=80)

        self.frame1.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel = SidePanel(master)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame1)

        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.show()


class Controller():

    def __init__(self):
        self.root = Tk.Tk()
        self.view = View(self.root)

        self.view.sidepanel.runBut.bind("<Button>", self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>", self.clear)

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

        self.view.sidepanel.label6.bind("<Label>")
        self.view.sidepanel.entree6.bind("<Entry>")

    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()

    def clear(self, event):
        self.view.ax0.clear()
       # self.cb.remove()

        self.view.fig.canvas.draw()

    def my_plot(self, event):

        radiusmin = int(self.view.sidepanel.entree1.get())
        radiusmax = int(self.view.sidepanel.entree2.get())
        radiusstep = float(self.view.sidepanel.entree3.get())
        anglemin = int(self.view.sidepanel.entree4.get())
        anglemax = int(self.view.sidepanel.entree5.get())
        anglestep = int(self.view.sidepanel.entree6.get())

        r = np.arange(radiusmin, radiusmax, radiusstep)
        theta = np.arange(anglemin,anglemax,anglestep)
        theta = theta / 180 * pi
        X = np.array([r]).transpose()*(np.sin(theta))
        Y = np.array([r]).transpose()*(np.cos(theta))
        Nr, Na =  X.shape
        Z = np.zeros((Nr, Na))

        self.label7 = Label(self.view.sidepanel.frame2, text="Nr")
        self.label7.pack(side="top", fill=Tk.BOTH)
        valeur7 = IntVar()
        valeur7.set(Nr)
        self.entree7 = Entry(self.view.sidepanel.frame2, textvariable=valeur7, width=10)
        self.entree7.pack(side="top", fill=Tk.BOTH)

        self.label8 = Label(self.view.sidepanel.frame2, text="Na")
        self.label8.pack(side="top", fill=Tk.BOTH)
        valeur8 = IntVar()
        valeur8.set(Na)
        self.entree8 = Entry(self.view.sidepanel.frame2, textvariable=valeur8, width=10)
        self.entree8.pack(side="top", fill=Tk.BOTH)

        itFrame = 1
        fps_debut = time()
        while (self.view.sidepanel.var1.get()==0):
            plt.xlabel('x[mm]')
            plt.ylabel('z[mm]')

            A = np.random.randn(Nr,Na)

            fps_fin = time()

            tframe=fps_fin-fps_debut
            self.FPS=itFrame / tframe
            itFrame = itFrame + 1

            minA = min(A.flatten(1))
            maxA = max(A.flatten(1))

            self.view.ax0.invert_yaxis()
            self.view.ax0.pcolormesh(X,Y,A, cmap='jet')
           # self.cb = self.view.fig.colorbar((self.c))

            self.label9 = Label(self.view.sidepanel.frame2, text="FPS ")
            self.label9.pack(side="top", fill=Tk.BOTH)
            self.label9.bind("<Label>")
            FPS_value = IntVar()
            FPS_value.set(round(self.FPS,2))
            self.entree9 = Entry(self.view.sidepanel.frame2, textvariable=FPS_value, width=10)
            self.entree9.pack(side="top", fill=Tk.BOTH)

            self.view.fig.canvas.draw()

            self.view.ax0.clear()

            self.label9.update()
            self.entree9.update()

            self.label9.destroy()
            self.entree9.destroy()

if __name__ == '__main__':
    c = Controller()
    c.run()
