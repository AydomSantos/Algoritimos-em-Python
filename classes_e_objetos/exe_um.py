class Bola:
    def __init__(self, pCor, pCircunferencia, pMaterial):
        self.pCor = pCor
        self.pCircunferencia = pCircunferencia
        self.pMaterial = pMaterial

    def setCor(self, pNova_cor):
        self.pCor = pNova_cor

    def getCor(self):
        return print(self.pCor)

    def mostra_info(self):
        print(f"A cor da Bola e : {self.pCor}")
        print(f"A circunferencia e: {self.pCircunferencia}")
        print(f"o material e: {self.pMaterial}")

bola_um = Bola("Vermelho", "Redonda", "Latex")
bola_um.setCor("Verde")
bola_um.getCor()