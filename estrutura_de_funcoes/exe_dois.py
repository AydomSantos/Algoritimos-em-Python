
vValor_usuario = int(input("Digite um valor: "))
def imprimir(vValor):
    for i in range(1, vValor + 1):
        print(str(i) * i)

imprimir(vValor_usuario)