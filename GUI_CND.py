from tkinter import *
from PIL import Image, ImageTk

## création de l'objet fenÍtre
fenetre = Tk()

## Frame1 pour le graphe 
Frame1 = Frame(fenetre, borderwidth=2, relief = GROOVE)
Frame1.pack(side=LEFT, padx=5, pady=5)

## Frame2 pour les boutons
Frame2 = Frame(fenetre, borderwidth=2, relief = RIDGE)
Frame2.pack(side=RIGHT, padx=30, pady=30)

image = Image.open("imageUS.png") #variable image qui prendra l'image png
graphe = ImageTk.PhotoImage(image) #objet graphe 
canvas = Canvas(Frame1,width=700,height=700) # dimensionnement du frame1 correspondant au graphe
canvas.create_image(400, 380, anchor=CENTER, image=graphe)
canvas.pack()


#permet de recuperer les 5 paramètres
def recupere():
    showinfo("Valeurs paramètres",entree1.get(),entree2.gey(),entree3.get(),entree4.get(),entree5.get())


## label correspondant à une fenetre avec son entrée qui représente les 5 paramètres de la vue matricielle

label1 = Label(Frame2, text="Position en x ")#label avec le texte de l'entrée
label1.pack()
xRef = StringVar()#variable d'entrée qu'on met à 0 en initial
xRef.set("0")
entree1 = Entry(Frame2, textvariable=xRef, width=10)#cadre pour taper la valeur souhaitée
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

##récupère les valeurs des 5 paramètres
valeurs = Button(Frame2, text="RUN", command=recupere)#objet bouton qui permettre de lancer le programme imageurUS
valeurs.pack()       

fenetre.mainloop()

