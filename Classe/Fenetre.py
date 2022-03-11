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

        self.filemenu = tk.Menu(menubar)
        self.filemenu.add_command(label="Reduce", command=lambda: self.fenetre.iconify())
        self.filemenu.add_command(label="Exit", command=lambda: self.fenetre.destroy())
        menubar.add_cascade(label="File", menu=self.filemenu)

        self.optionmenu = tk.Menu(menubar)
        self.optionmenu.add_command(label="Colors", command=lambda: self.Inter())
        self.optionmenu.add_command(label="Config")
        self.optionmenu.add_command(label="Fullscreen", command=lambda: self.fs())
        menubar.add_cascade(label="Options", menu=self.optionmenu)

        self.intmenu = tk.Menu(menubar)
        self.intmenu.add_command(label="Help", command=lambda: os.startfile('readme.md'))
        self.intmenu.add_command(label="About", command=lambda: webbrowser.open('https://github.com/Woodlutins/MachinePingu'))
        self.intmenu.add_command(label="Report bug", command=lambda: webbrowser.open('https://github.com/Woodlutins/MachinePingu/issues'))
        menubar.add_cascade(label="?", menu=self.intmenu)

        self.fenetre.config(menu=menubar)

    def fs(self):
        self.fullScreenState = not self.fullScreenState
        self.fenetre.attributes("-fullscreen", self.fullScreenState)

    def Inter(self):
        self.optionmenu.entryconfig(1, state=tk.DISABLED)
        self.Int = OptionGraphique(self.fenetre, self.optionmenu)
        self.Int.Fenetre.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.Int.Fenetre.mainloop()
    def on_closing(self):
        self.Int.Annuler()
