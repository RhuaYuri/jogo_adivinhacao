import tkinter as t
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from PIL import Image
from PIL import ImageTk
from time import sleep
from util.Funcao import Funcao as f

class PorImagens:
    def __init__(self):
        pass
    def Imagens(self, root, listImagem, var):
        self.root = root
        self.listImagem = listImagem
        self.funcao = f()
        if var == 0:
            self.img1 = Image.open(self.listImagem[0])
            self.img1 = ImageTk.PhotoImage(self.img1)
            self.button1 = t.Button(image=self.img1,
                                command=lambda: 
                                self.compararImagem(self.listImagem[0], self.listImagem, 0)
                                ).place(x=12, y=50)
        elif var == 1:
            self.img2 = Image.open(self.listImagem[1])
            self.img2 = ImageTk.PhotoImage(self.img2)
            self.button2 = t.Button(image=self.img2,
                                command=lambda: 
                                self.compararImagem(self.listImagem[1], self.listImagem, 1)
                                ).place(x=238, y=50)
        elif var == 2:
            self.img3 = Image.open(self.listImagem[2])
            self.img3 = ImageTk.PhotoImage(self.img3)
            self.button3 = t.Button(image=self.img3,
                                command=lambda: 
                                self.compararImagem(self.listImagem[2], self.listImagem, 2)
                                ).place(x=462, y=50)
        elif var == 3:
            self.img4 = Image.open(self.listImagem[3])
            self.img4 = ImageTk.PhotoImage(self.img4)
            self.button4 = t.Button(image=self.img4,
                                command=lambda: 
                                self.compararImagem(self.listImagem[3], self.listImagem, 3)
                                ).place(x=684, y=50)
        elif var == 4:     
            self.img5 = Image.open(self.listImagem[4])
            self.img5 = ImageTk.PhotoImage(self.img5)
            self.button5 = t.Button(image=self.img5,
                                command=lambda: 
                                self.compararImagem(self.listImagem[4], self.listImagem, 4)
                                ).place(x=12, y=300)
        elif var == 5:
            self.img6 = Image.open(self.listImagem[5])
            self.img6 = ImageTk.PhotoImage(self.img6)
            self.button6 = t.Button(image=self.img6,
                                command=lambda: 
                                self.compararImagem(self.listImagem[5], self.listImagem, 5)
                                ).place(x=238, y=300)
        elif var == 6:
            self.img7 = Image.open(self.listImagem[6])
            self.img7 = ImageTk.PhotoImage(self.img7)
            self.button7 = t.Button(image=self.img7,
                                command=lambda: 
                                self.compararImagem(self.listImagem[6], self.listImagem, 6)
                                ).place(x=462, y=300)
        elif var == 7:
            self.img8 = Image.open(self.listImagem[7])
            self.img8 = ImageTk.PhotoImage(self.img8)
            self.button8 = t.Button(image=self.img8,
                                command=lambda: 
                                self.compararImagem(self.listImagem[7], self.listImagem, 7)
                                ).place(x=684, y=300)
            self.rescursoIcone.icone(self.root)

    def compararImagem(self, cam, lista, var):
        self.funcao.compararImagem(self.root, cam, lista, var)

