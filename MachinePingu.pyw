import platform
import subprocess
import os
import tkinter as tk
import time

def BigPing(ip): #Fait un ping, id = l'id ping ensuite retourne False ou True en fonction de la réponse du ping
    with open(os.devnull, "wb") as limbo:
        p=subprocess.Popen(["ping","-n","1", "-w", "2", ip], stdout=limbo, stderr=limbo).wait()
        if p:
            return False
        else:
            return True

class Box(tk.Frame) :
    def __init__(self, nom):
        self.nom = nom
        self.Frame = tk.Frame(fenetre, bg=FondBox)
        labelNom = tk.Label(self.Frame, bg=FondNom, fg=CouleurTexte, text=self.nom, font=("Arial Black",18)).pack(fill="both", pady=5, padx=5)
        self.Frame.pack(fill="both", pady=5, padx=5)

class Reseau(tk.Frame):
    def __init__(self, frameParent, nom, ip):
        self.Frame = tk.Frame(frameParent.Frame)
        self.nom = nom
        self.ip = ip
        self.Frame.bind('<Button 1>', lambda e: self.reload())
        labelNom = tk.Label(self.Frame, fg=CouleurTexte, text=self.nom, font=18).pack()
        labelNom = tk.Label(self.Frame, fg=CouleurTexte, text=self.ip).pack()
        self.Frame.pack(side=tk.LEFT, fill="both", expand=True, pady=5, padx=5)
        self.reload()
        
    def reload(self):
        if BigPing(self.ip):
            self.refreshColor(CouleurUp)
        else:
            self.refreshColor(CouleurDown)
        fenetre.after(30000, self.reload)
        
    def refreshColor(self, color):
        FL = self.Frame.winfo_children()
        self.Frame['bg']=color
        for F in FL:
            F['bg']=color

#Interface Graphique    
FondFenetre = 'black'
FondBox = 'darkslategray'
FondNom = 'slategray'
CouleurUp = 'green'
CouleurDown = 'red'
CouleurTexte = 'lightgray'

fenetre = tk.Tk()
fenetre.configure(bg=FondFenetre)
fenetre.bind('<Escape>',lambda e: fenetre.destroy())
fenetre.geometry('800x400')

BoxP = Box("Box Principale") #Ajoutez une Box 
ReseauInt = Reseau(BoxP,"Internet", "172.1.1.1") #Ajoutez un Réseau
ReseauSOS = Reseau(BoxP,"Secours", "172.2.2.1")
ReseauPri = Reseau(BoxP,"Privée", "192.154.10.25")

BoxS = Box("Box Secondaire")
ReseauInt = Reseau(BoxS,"Internet", "192.126.39.120")

BoxT = Box("Box Test")
ReseauInt = Reseau(BoxT,"Internet", "80.13.250.238")
ReseauLan = Reseau(BoxT,"Lan", "192.52.12.36")


fenetre.mainloop()
