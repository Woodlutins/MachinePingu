import tkinter as tk

class Box(tk.Frame) :
    def __init__(self, fenetre, nom):
        self.nom = nom
        self.fenetre = fenetre
        
        self.Frame = tk.Frame(fenetre.fenetre, bg=fenetre.FondBox)
        labelNom = tk.Label(self.Frame, bg=fenetre.FondNom, fg=fenetre.CouleurTexte, text=self.nom, font=("Arial Black",18)).pack(fill="both", pady=5, padx=5)
        self.Frame.pack(fill="both", pady=5, padx=5)
