import tkinter as tk

class Fenetre(tk.Tk) :
    def __init__(self, nom):
        self.nom = nom
        self.FondFenetre = 'black'
        self.FondBox = 'darkslategray'
        self.FondNom = 'slategray'
        self.CouleurUp = 'green'
        self.CouleurDown = 'red'
        self.CouleurTexte = 'lightgray'

        self.fenetre = tk.Tk()
        self.fenetre.configure(bg=self.FondFenetre)
        self.fenetre.bind('<Escape>',lambda e: fenetre.destroy())
        self.fenetre.geometry('800x400')
