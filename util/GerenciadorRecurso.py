import os



class GerenciadorRecurso:
    DIRETORIO_RAIZ = os.path.realpath('..')
    PASTA = 'img'
    ORIGEM = 'jogo_adivinhacao'
    ICONE = 'icone.jpg'

    def __init__(self):
        pass
    def carregarImagens(self):
        self.lista = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
        self.lista1 = []
        for IMAGEM in self.lista:
            img = os.path.join(self.PASTA, IMAGEM)
            self.lista1.append(self.montarCaminhoRecurso(img))
        return self.lista1

    def IconeM(self):
        icone = os.path.join(self.PASTA, self.ICONE)
        return self.montarCaminhoRecurso(icone)

    def montarCaminhoRecurso(self, nomeRecurso):
        return os.path.join(self.DIRETORIO_RAIZ, self.ORIGEM, nomeRecurso)

