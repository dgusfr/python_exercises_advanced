class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f'Ponto: ({self.x}, {self.y})')


class Retangulo:
    def __init__(self, largura, altura, ponto):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto
    
    def encontrar_centro(self):
        centro_x = self.ponto.x + self.largura / 2
        centro_y = self.ponto.y + self.altura / 2
        return Ponto(centro_x, centro_y)
        
ponto = Ponto(2, 3)
ponto.imprimir()

retangulo = Retangulo(5, 4, ponto)
centro = retangulo.encontrar_centro()
print(f'O centro do retângulo é:')
centro.imprimir()
