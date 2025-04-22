class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos) :
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.05 * anos
            print(f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura:.2f}")
        else:
            print(f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura:.2f}")

    def engordar(self, peso):
        self.peso += peso
        print(f"Nome: {self.nome}, Peso: {self.peso}")

    def emagrecer(self, peso):
        self.peso -= peso
        print(f"Nome: {self.nome}, Peso: {self.peso}")

    def crescer(self, altura):
        self.altura += altura
        print(f"Nome: {self.nome}, Altura: {self.altura:.2f}")


pessoa_um = Pessoa("João", 15, 60, 1.60)
pessoa_um.envelhecer(15)

pessoa_dois = Pessoa("Maria", 25, 55, 1.65)
pessoa_dois.engordar(15)

pessoa_tres = Pessoa("Pedro", 30, 70, 1.70)
pessoa_tres.crescer(0.10)

