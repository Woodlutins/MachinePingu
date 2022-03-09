import tkinter as tk
from Classe.InterfaceGraphique import *

class Bouton(tk.Button) :
    def __init__(self, Reseau, is_Visible):
        self.Reseau = Reseau
        self.is_Visible = is_Visible
        self.Button = tk.Button(self.Reseau.Frame, fg=Color[3], text="Modififer", command = self.OpenFenMod())
        self.SwitchButton()

    def SwitchButton(self):
        if (self.is_Visible == False):
            self.Button.pack(side=tk.RIGHT)
            self.is_Visible = True
        else:
            self.Button.pack_forget()
            self.is_Visible = False
    def OpenFenMod(self):
        #nothing
        read = 1
