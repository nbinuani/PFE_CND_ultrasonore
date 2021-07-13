from tkinter import *
from PIL import Image, ImageTk

## création de l'objet fenÍtre
fenetre = Tk()

def afficher(figure):
    image = Image.open(figure)
    graphe = ImageTk.PhotoImage(image)
    canvas.create_image(400,380, image=graphe)
    canvas = Canvas(fenetre,width=600,height=1000)
    canvas.pack()

bouton = Button(fenetre, text="RUN",command=afficher("imageUS.png"))
bouton.pack()

fenetre.mainloop()
