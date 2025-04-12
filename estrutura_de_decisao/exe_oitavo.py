# Get input from user
valor_um = int(input("Digite o primeiro valor: "))
valor_dois = int(input("Digite o segundo valor: "))
valor_tres = int(input("Digite o terceiro valor: "))

menor_valor = min(valor_um, valor_dois, valor_tres)
maior_valor = max(valor_um, valor_dois, valor_tres)

print(f"\nO menor valor é: {menor_valor}")
print(f"O maior valor é: {maior_valor}")