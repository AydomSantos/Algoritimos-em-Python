def calcular_area_dobro(lado):
    area = lado * lado
    dobro_area = 2 * area
    return dobro_area

lado = float(input("Digite o comprimento do lado do quadrado: "))
resultado = calcular_area_dobro(lado)
print("O dobro da área do quadrado é:", resultado)
