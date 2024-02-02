class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
        

    def mudaLado(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def retornaLado(self):
        print(f'O novo lado do quadrado é:', self.tamanhoLado)

    def calculaArea(self):
        area = self.tamanhoLado * self.tamanhoLado
        print('A area do quadrado é:', area)
        


quadrado = Quadrado(20)
quadrado.mudaLado(40)
quadrado.retornaLado()
quadrado.calculaArea()

