vIdade_usuario = int(input("Digite a sua idade: "))
if vIdade_usuario > 18:
    print("maior de idade")
else:
    if vIdade_usuario < 12:
        print("criança")
    elif vIdade_usuario > 12:
        print("adolecente")