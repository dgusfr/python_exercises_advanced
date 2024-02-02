class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(f'A cor seloecionada é:', self.cor)

bola = Bola("verde", 20, 'plastico' )
bola.trocaCor("Azul")
bola.mostraCor()