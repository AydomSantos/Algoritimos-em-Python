
produto_1 = input("Digite o nome do primeiro produto: ")
preco_1 = float(input(f"Digite o preço de {produto_1}: "))

produto_2 = input("Digite o nome do segundo produto: ")
preco_2 = float(input(f"Digite o preço de {produto_2}: "))

produto_3 = input("Digite o nome do terceiro produto: ")
preco_3 = float(input(f"Digite o preço de {produto_3}: "))

produto_mais_barato = min(preco_1, preco_2, preco_3)
print("\nRecomendação de compra:")
print(f"Você deve comprar {produto_mais_barato} pois é o produto mais econômico, custando R$ {produto_mais_barato:.2f}")