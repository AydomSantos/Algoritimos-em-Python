vNota_um = float(input("Digite a primeira nota: "))
vNota_dois = float(input("Digite a segunda nota: "))
vNota_tres = float(input("Digite a terceira nota: "))


media = (vNota_um + vNota_dois + vNota_tres) / 3
if media >= 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")