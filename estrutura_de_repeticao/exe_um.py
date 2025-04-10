vNota = int(input("Digite uma nota: "))

while vNota < 0 or vNota > 10:
    print("Nota inválida")
    vNota = int(input("Digite uma nota: "))

print("Nota Ok")
