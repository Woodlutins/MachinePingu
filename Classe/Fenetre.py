import tkinter as tk
import webbrowser
import os
from Classe.InterfaceGraphique import *


class Fenetre(tk.Tk) :
    def __init__(self, nom):
        self.nom = nom
        self.fullScreenState=False
        self.fenetre = tk.Tk()
        self.fenetre.configure(bg=Color[0])
        self.fenetre.bind('<Escape>',lambda e: self.fenetre.destroy())
        self.fenetre.bind('<F11>',lambda e: self.fs())
        self.fenetre.geometry('800x400')

        menubar = tk.Menu(self.fenetre)

        filemenu = tk.Menu(menubar)
        filemenu.add_command(label="Reduce", command=lambda: self.fenetre.iconify())
        filemenu.add_command(label="Exit", command=lambda: self.fenetre.destroy())
        menubar.add_cascade(label="File", menu=filemenu)

        optionmenu = tk.Menu(menubar)
        optionmenu.add_command(label="Color", command=lambda: self.Inter())
        optionmenu.add_command(label="Config")
        optionmenu.add_command(label="Fullscreen", command=lambda: self.fs())
        menubar.add_cascade(label="Options", menu=optionmenu)

        intmenu = tk.Menu(menubar)
        intmenu.add_command(label="Help", command=lambda: os.startfile('readme.md'))
        intmenu.add_command(label="About", command=lambda: webbrowser.open('https://github.com/Woodlutins/MachinePingu'))
        intmenu.add_command(label="Report bug", command=lambda: webbrowser.open('https://github.com/Woodlutins/MachinePingu/issues'))
        menubar.add_cascade(label="?", menu=intmenu)

        self.fenetre.config(menu=menubar)

    def fs(self):
        self.fullScreenState = not self.fullScreenState
        self.fenetre.attributes("-fullscreen", self.fullScreenState)

    def Inter(self):

        #print(self.Int.Fenetre.winfo_exists())
        #if self.Int.Fenetre.winfo_exists():
            #self.Int.Fenetre.destroy()
        self.Int = OptionGraphique(self.fenetre)

        self.Int.Fenetre.mainloop()
