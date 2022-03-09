import tkinter as tk
from Classe.InterfaceGraphique import *

class Label(tk.Label) :
    def __init__(self, FrameParent, text):
        self.text = text
        self.Frame= FrameParent
        self.Label = tk.Label(self.Frame.Frame, fg=Color[3], text=self.text, font=18)
        self.Label.pack()

    def setText(self, T):
        self.text = T
        self.Label['text']=self.text
