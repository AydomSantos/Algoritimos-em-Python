vValor_um = int(input("Digite o primeiro valor: "))
vValor_dois = int(input("Digite o segundo valor: "))
vValor_tres = int(input("Digite o terceiro valor: "))

vValores_decrescente = [vValor_um, vValor_dois, vValor_tres]

if vValor_um < 0 or vValor_dois < 0 or vValor_tres < 0:
    print("Somente valores positivos são permitidos.")
else:
    print("Os valores digitados foram:")
    for valor in sorted(vValores_decrescente, reverse=True):
        print(valor)