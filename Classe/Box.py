import tkinter as tk
from Classe.InterfaceGraphique import *

class Box(tk.Frame) :
    def __init__(self, fenetre, nom):
        self.nom = nom
        self.fenetre = fenetre

        self.Frame = tk.Frame(fenetre.fenetre, bg=Color[1])
        tk.Label(self.Frame, bg=Color[2], fg=Color[3], text=self.nom, font=("Arial Black",18)).pack(fill="both", pady=5, padx=5)
        self.Frame.pack(fill="both", pady=5, padx=5)
