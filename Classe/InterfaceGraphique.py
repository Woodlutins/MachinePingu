import tkinter as tk
from tkinter.colorchooser import askcolor
import os

def loadConfig():
    file1 = open('Classe/config.txt', 'r')
    lines = file1.readlines()
    file1.close()
    i=0
    global Color
    for line in lines:
        Color[i]=line[:-1]
        i+=1

class OptionGraphique(tk.Tk) :
    def __init__(self, fParent, OptionMenu):
        self.Fenetre = tk.Toplevel(fParent)
        self.OM=OptionMenu
        F = tk.Frame(self.Fenetre)
        tk.Label(F, text="FondFenetre", width=10).pack(side=tk.LEFT)
        BtnChg0 = tk.Button(F, text="", bg=Color[0], width=10, command = lambda: self.change_color(BtnChg0))
        BtnChg0.pack(side=tk.LEFT)
        F.pack()

        F = tk.Frame(self.Fenetre)
        tk.Label(F, text="FondBox", width=10).pack(side=tk.LEFT)
        BtnChg1 = tk.Button(F, text="", bg=Color[1], width=10, command = lambda: self.change_color(BtnChg1))
        BtnChg1.pack(side=tk.LEFT)
        F.pack()

        F = tk.Frame(self.Fenetre)
        tk.Label(F, text="FondNom", width=10).pack(side=tk.LEFT)
        BtnChg2 = tk.Button(F, text="", bg=Color[2], width=10, command = lambda: self.change_color(BtnChg2))
        BtnChg2.pack(side=tk.LEFT)
        F.pack()

        F = tk.Frame(self.Fenetre)
        tk.Label(F, text="CouleurTexte", width=10).pack(side=tk.LEFT)
        BtnChg3 = tk.Button(F, text="", bg=Color[3], width=10, command = lambda: self.change_color(BtnChg3))
        BtnChg3.pack(side=tk.LEFT)
        F.pack()

        F = tk.Frame(self.Fenetre)
        tk.Label(F, text="CouleurUp", width=10).pack(side=tk.LEFT)
        BtnChg4 = tk.Button(F, text="", bg=Color[4], width=10, command = lambda: self.change_color(BtnChg4))
        BtnChg4.pack(side=tk.LEFT)
        F.pack()

        F = tk.Frame(self.Fenetre)
        tk.Label(F, text="CouleurDown", width=10).pack(side=tk.LEFT)
        BtnChg5 = tk.Button(F, text="", bg=Color[5], width=10, command = lambda: self.change_color(BtnChg5))
        BtnChg5.pack(side=tk.LEFT)
        F.pack()

        F = tk.Frame(self.Fenetre)
        tk.Label(F, text="CouleurTest", width=10).pack(side=tk.LEFT)
        BtnChg6 = tk.Button(F, text="", bg=Color[6], width=10, command = lambda: self.change_color(BtnChg6))
        BtnChg6.pack(side=tk.LEFT)
        F.pack()

        F = tk.Frame(self.Fenetre)
        tk.Button(F, text="Valider", command = lambda: self.Valider()).pack(side=tk.LEFT, padx="5")
        tk.Button(F, text="Annuler", command = lambda: self.Annuler()).pack(side=tk.LEFT,padx="5")
        F.pack()


    def change_color(self, Btn):
        colors = askcolor(title="Color Chooser")
        if colors[1]:
            i=0
            for Col in Color:
                if Col == Btn['bg']:
                    C = i
                i+=1

            self.ModifLigne(C, colors[1])
            loadConfig()
            Btn['bg' ]= colors[1]

    def ModifLigne(self, OldLine, Newline):
        file1 = open('Classe/config.txt', 'r')
        lines = file1.readlines()
        file1.close()
        fichier = open("Classe/buff.txt", "a")
        for line in lines:
            if line[:-1] == Color[OldLine]:
                fichier.write(Newline+"\n")
            else:
                fichier.write(line)
        fichier.close()

    def Valider(self):
        try:
            with open("Classe/buff.txt"): pass
            os.remove("Classe/config.txt")
            os.rename("Classe/buff.txt","Classe/config.txt")
        except IOError: pass
        self.OM.entryconfig(1, state=tk.NORMAL)
        self.Fenetre.destroy()

    def Annuler(self):
        try:
            with open("Classe/buff.txt"): pass
            os.remove("Classe/buff.txt")
        except IOError: pass
        self.OM.entryconfig(1, state=tk.NORMAL)
        self.Fenetre.destroy()

##-CODE-SPECIALE-##
Color=[0,0,0,0,0,0,0]
loadConfig()
