class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def MudaLado(self, base, altura):
        self.base = base
        self.altura = altura

    def retornaNovosLados(self):
        print("A nova base mede:", self.base)
        print("A nova altura mede:", self.altura)

    def calculaArea(self):
        area = self.base * self.altura
        print('A area do retangulo é:', area)

    def calculaPerimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print('O perimetro do retangulo é:', perimetro)

retangulo = Retangulo(10, 7)
retangulo.calculaArea()
retangulo.calculaPerimetro()

retangulo.MudaLado(20, 14)
retangulo.retornaNovosLados()
retangulo.calculaArea()
retangulo.calculaPerimetro()



