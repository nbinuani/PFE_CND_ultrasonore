import tkinter as Tk 
root = Tk.Tk() 
lbl = Tk.Label(text=0) 
def go(): 
    for i in range(100000): 
        lbl.config(text=i) 
        root.update()     
btn = Tk.Button(text='go', command=go) 
lbl.pack() 
btn.pack() 
root.mainloop()
