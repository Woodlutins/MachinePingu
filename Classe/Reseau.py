import tkinter as tk
import time
import platform
import subprocess
import os

class Reseau(tk.Frame):
    def __init__(self, frameParent, nom, ip):
        self.Frame = tk.Frame(frameParent.Frame)
        self.nom = nom
        self.ip = ip
        self.frameParent = frameParent
        
        self.Frame.bind('<Button 1>', lambda e: self.reload())
        labelNom = tk.Label(self.Frame, fg=frameParent.fenetre.CouleurTexte, text=self.nom, font=18).pack()
        labelNom = tk.Label(self.Frame, fg=frameParent.fenetre.CouleurTexte, text=self.ip).pack()
        self.Frame.pack(side=tk.LEFT, fill="both", expand=True, pady=5, padx=5)
        self.reload()

    def reload(self):
        if self.BigPing(self.ip):
            self.refreshColor(self.frameParent.fenetre.CouleurUp)
        else:
            self.refreshColor(self.frameParent.fenetre.CouleurDown)
        self.frameParent.fenetre.fenetre.after(30000, self.reload)

    def refreshColor(self, color):
        FL = self.Frame.winfo_children()
        self.Frame['bg']=color
        for F in FL:
            F['bg']=color

    def BigPing(self, ip): #Fait un ping, id = l'id ping ensuite retourne False ou True en fonction de la réponse du ping
        with open(os.devnull, "wb") as limbo:
            p=subprocess.Popen(["ping","-n","1", "-w", "2", ip], stdout=limbo, stderr=limbo).wait()
            if p:
                return False
            else:
                return True
