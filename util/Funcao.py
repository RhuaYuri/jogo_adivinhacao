import tkinter as t 
from time import sleep

class Funcao:
    def __init__(self):
        pass
    def compararImagem(self, root, cam, lista, var, icone=None):
        from util.PorImagens import PorImagens as PI
        from util.ReporIcone import ReporIcone as RI
        self.root = root
        self.rescursoImagem = PI()
        self.recursoIcone = RI()
        self.camIcone = icone
        if self.x == '':
            self.x = cam
        elif self.y == ' ':
            self.y = cam
        self.rescursoImagem.Imagens(self.root, lista, var)
        if self.x != '' and self.y != ' ':
            if self.x != self.y:
                self.rescursoImagem.Imagens(self.root, lista, var)
                sleep(5)
                self.recursoIcone.IconeNovo(self.root, self.camIcone)