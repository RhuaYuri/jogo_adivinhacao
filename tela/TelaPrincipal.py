import tkinter as t 
from random import randint
from PIL import Image
from PIL import ImageTk
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from time import sleep

class TelaPrincipal():
    cont = 0
    def __init__(self):
        self.anterior = 0
        
        self.cont += 1
        self.x = ''
        self.y = ' '
        self.local1X = 0
        self.local2X = 0
        self.local1Y = 0
        self.local2Y = 0
        self.local1x = 12
        self.local2x = 238
        self.local3x = 462
        self.local4x = 684
        self.local1y = 50
        self.local2y = 300
        self.root = t.Tk()
        self.root.geometry('900x600')
        self.titulo = t.Label(self.root, text='Jogo da Adivinhação', font='arial 20 bold').pack()
        self.recurso = gr()
        self.caminhos = self.recurso.carregarImagens()
        self.listImagem = self.escolherImagem()
        

        self.recurso = gr()
        self.camIcone = self.recurso.IconeM()
        self.listaAcertos = []
        for i in range(8):
            self.listaAcertos.append(self.camIcone)
        self.img1 = Image.open(self.camIcone)
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.button1 = t.Button(image=self.img1,
                                command=lambda: 
                                self.compararImagem(self.listImagem[0], self.listImagem, 0)
                                ).place(x=self.local1x, y=self.local1y)

        self.img2 = Image.open(self.camIcone)
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.button2 = t.Button(image=self.img2,
                                command=lambda: 
                                self.compararImagem(self.listImagem[1], self.listImagem, 1)
                                ).place(x=self.local2x, y=self.local1y)

        self.img3 = Image.open(self.camIcone)
        self.img3 = ImageTk.PhotoImage(self.img3)
        self.button3 = t.Button(image=self.img3,
                                command=lambda: self.compararImagem(self.listImagem[2], self.listImagem, 2)
                                ).place(x=self.local3x, y=self.local1y)

        self.img4 = Image.open(self.camIcone)
        self.img4 = ImageTk.PhotoImage(self.img4)
        self.button4 = t.Button(image=self.img4,
                                command=lambda: self.compararImagem(self.listImagem[3], self.listImagem, 3)
                                ).place(x=self.local4x, y=self.local1y)
        
        self.img5 = Image.open(self.camIcone)
        self.img5 = ImageTk.PhotoImage(self.img5)
        self.button5 = t.Button(image=self.img5,
                                command=lambda: self.compararImagem(self.listImagem[4], self.listImagem, 4)
                                ).place(x=self.local1x, y=self.local2y)

        self.img6 = Image.open(self.camIcone)
        self.img6 = ImageTk.PhotoImage(self.img6)
        self.button6 = t.Button(image=self.img6,
                                command=lambda: self.compararImagem(self.listImagem[5], self.listImagem, 5)
                                ).place(x=self.local2x, y=self.local2y)

        self.img7 = Image.open(self.camIcone)
        self.img7 = ImageTk.PhotoImage(self.img7)
        self.button7 = t.Button(image=self.img7,
                                command=lambda: self.compararImagem(self.listImagem[6], self.listImagem, 6)
                                ).place(x=self.local3x, y=self.local2y)

        self.img8 = Image.open(self.camIcone)
        self.img8 = ImageTk.PhotoImage(self.img8)
        self.button8 = t.Button(image=self.img8,
                                command=lambda: self.compararImagem(self.listImagem[7], self.listImagem, 7)
                                ).place(x=self.local4x, y=self.local2y)

        self.root.mainloop()

    def compararImagem(self, cam, lista, var):
        if self.x == '':
            self.x = cam
            self.anterior = var
        elif self.y == ' ':
            self.y = cam
        self.Imagens(var)
        self.listaAcertos[var] = self.listImagem[var]
        if self.x != '' and self.y != ' ':
            if self.listImagem[self.anterior] != self.listImagem[var]:
                self.listaAcertos[var] = self.camIcone
                self.listaAcertos[self.anterior] = self.camIcone
                self.anterior = 0
                self.IconeNovo()
            self.x = ''
            self.y = ' '
         
    
    def escolherImagem(self):
        self.listaRetorno = []
        self.cont = 0
        self.ListaControle = [0, 1, 2, 3]
        self.cont1 = 0
        self.cont2 = 0
        self.cont3 = 0
        self.cont4 = 0
        self.ver = 0
        for i in range(8):
            while True:
                self.ImagemEscolhida = randint(0, 3)
                if self.ImagemEscolhida == 0:
                    if self.cont1 != 2:
                        self.listaRetorno.append(self.caminhos[self.ImagemEscolhida])
                        self.cont1 += 1
                        break
                if self.ImagemEscolhida == 1:
                    if self.cont2 != 2:
                        self.listaRetorno.append(self.caminhos[self.ImagemEscolhida])
                        self.cont2 += 1
                        break

                elif self.ImagemEscolhida == 2:
                    if self.cont3 != 2:
                        self.listaRetorno.append(self.caminhos[self.ImagemEscolhida])
                        self.cont3 += 1
                        break
                elif self.ImagemEscolhida == 3: 
                    if self.cont4 != 2:
                        self.listaRetorno.append(self.caminhos[self.ImagemEscolhida])
                        self.cont4 += 1
                        break
        return self.listaRetorno

    def IconeNovo(self):
        self.img1 = Image.open(self.listaAcertos[0])
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.button1 = t.Button(image=self.img1,
                                command=lambda: 
                                self.compararImagem(self.listaAcertos[0], self.listImagem, 0)
                                ).place(x=self.local1x, y=self.local1y)

        self.img2 = Image.open(self.listaAcertos[1])
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.button2 = t.Button(image=self.img2,
                                command=lambda: 
                                self.compararImagem(self.listaAcertos[1], self.listImagem, 1)
                                ).place(x=self.local2x, y=self.local1y)

        self.img3 = Image.open(self.listaAcertos[2])
        self.img3 = ImageTk.PhotoImage(self.img3)
        self.button3 = t.Button(image=self.img3,
                                command=lambda: self.compararImagem(self.listaAcertos[2], self.listImagem, 2)
                                ).place(x=self.local3x, y=self.local1y)

        self.img4 = Image.open(self.listaAcertos[3])
        self.img4 = ImageTk.PhotoImage(self.img4)
        self.button4 = t.Button(image=self.img4,
                                command=lambda: self.compararImagem(self.listaAcertos[3], self.listImagem, 3)
                                ).place(x=self.local4x, y=self.local1y)
        
        self.img5 = Image.open(self.listaAcertos[4])
        self.img5 = ImageTk.PhotoImage(self.img5)
        self.button5 = t.Button(image=self.img5,
                                command=lambda: self.compararImagem(cam=self.listaAcertos[4], lista=self.listImagem, var=4)
                                ).place(x=self.local1x, y=self.local2y)

        self.img6 = Image.open(self.listaAcertos[5])
        self.img6 = ImageTk.PhotoImage(self.img6)
        self.button6 = t.Button(image=self.img6,
                                command=lambda: self.compararImagem(self.listaAcertos[5], self.listImagem, 5)
                                ).place(x=self.local2x, y=self.local2y)

        self.img7 = Image.open(self.listaAcertos[6])
        self.img7 = ImageTk.PhotoImage(self.img7)
        self.button7 = t.Button(image=self.img7,
                                command=lambda: self.compararImagem(self.listaAcertos[6], self.listImagem, 6)
                                ).place(x=self.local3x, y=self.local2y)

        self.img8 = Image.open(self.listaAcertos[7])
        self.img8 = ImageTk.PhotoImage(self.img8)
        self.button8 = t.Button(image=self.img8,
                                command=lambda: self.compararImagem(self.listaAcertos[7], self.listImagem, 7)
                                ).place(x=self.local4x, y=self.local2y)


    def Imagens(self, var):
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

