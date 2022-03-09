import tkinter as tk
import time
import platform
import subprocess
import os
from Classe.Bouton import *
from Classe.Label import *
from Classe.InterfaceGraphique import *

class Reseau(tk.Frame):
    def __init__(self, frameParent, nom, ip):
        self.Frame = tk.Frame(frameParent.Frame)
        self.frameParent = frameParent

        self.Frame.bind('<Button 1>', lambda e: self.reload())
        self.LabelNom = Label(self, nom)
        self.LabelIp = Label(self, ip)

        BoutonMod = Bouton(self, True)
        self.Frame.bind('<Button 3>', lambda e: BoutonMod.SwitchButton())
        self.Frame.pack(side=tk.LEFT, fill="both", expand=True, pady=5, padx=5)
        self.AutoLoad()


    def AutoLoad(self):
        self.reload()
        self.frameParent.fenetre.fenetre.after(30000, self.reload)

    def reload(self):
        self.refreshColor(Color[6])
        self.Frame.update()
        if self.BigPing(self.LabelIp.text):
            self.refreshColor(Color[4])
        else:
            self.refreshColor(Color[5])

    def refreshColor(self, color):
        FL = self.Frame.winfo_children()
        self.Frame['bg']=color
        for F in FL:
            F['bg']=color

    def BigPing(self, ip): #Fait un ping, id = l'id ping ensuite retourne False ou True en fonction de la réponse du ping
        with open(os.devnull, "wb") as limbo:
            p=subprocess.Popen(["ping","-n","1", "-w", "2", ip], stdout=limbo, stderr=limbo, shell=True).wait()
            return not p
