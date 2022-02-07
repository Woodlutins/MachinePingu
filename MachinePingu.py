import tkinter as tk
from Classe.Box import *
from Classe.Reseau import *
from Classe.Fenetre import *


fenetre = Fenetre("Machine Pingu")

BoxP = Box(fenetre, "Box Principale") #Ajoutez une Box
ReseauInt = Reseau(BoxP,"Internet", "172.1.1.1") #Ajoutez un Réseau
ReseauSOS = Reseau(BoxP,"Secours", "172.2.2.1")
ReseauPri = Reseau(BoxP,"Privée", "192.154.10.25")

BoxS = Box(fenetre, "Box Secondaire")
ReseauInt = Reseau(BoxS,"Internet", "192.126.39.120")

BoxT = Box(fenetre, "Box Test")
ReseauInt = Reseau(BoxT,"Internet", "80.13.250.238")
ReseauLan = Reseau(BoxT,"Lan", "192.52.12.36")

fenetre.fenetre.mainloop()
