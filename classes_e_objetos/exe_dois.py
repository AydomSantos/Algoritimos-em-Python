class Quadrado:
    def __init__(self, tamanho, lado):
        self.tamanho = tamanho
        self.lado = lado
    def getQuadrado(self):
        return self.lado
    def setLado(self, pValor):
        self.lado = pValor
        print(f"O novo valor e: {pValor}")
    def calcularArea(self):
        vResultado = self.lado ** 2
        return print(f"O resultado da soma e {vResultado}")

meu_quadrado = Quadrado(0, 4)

# Testando os métodos
print(f"Lado do quadrado: {meu_quadrado.getQuadrado()}")
meu_quadrado.setLado(10)
meu_quadrado.calcularArea()