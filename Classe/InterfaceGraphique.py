import tkinter as tk
from tkinter.colorchooser import askcolor

with open('Classe/config.txt') as f:
    lines = f.readlines()

i=0
Color=[0,0,0,0,0,0,0,0,0]
for line in lines:
    Color[i]=line[:-1]
    i+=1
    
class OptionGraphique(tk.Tk) :
    def __init__(self, fParent):
        self.Fenetre = tk.Toplevel(fParent)

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

    def change_color(self, Btn):
        colors = askcolor(title="Color Chooser")

        for line in lines:
            if line[:-1] == Color[0]:
                print(line)
                line = line.replace(line, colors[1])


        Color[0] = colors[1]
        Btn['bg']=Color[0]
