# Função para verificar a maioridade
def verificar_maioridade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

# Função para verificar o tipo de pessoa com base na idade
def verificar_tipo_pessoa(idade):
    if idade < 18:
        return "Você é menor de idade."
    elif 18 <= idade < 65:
        return "Você é um adulto."
    else:
        return "Você é um idoso."

# Função para verificar se a pessoa pode comprar com ou sem cartão
def verificar_compra(idade, tem_cartao):
    if idade >= 18:
        if tem_cartao:
            return "Você pode comprar o produto."
        else:
            return "Você não pode comprar o produto sem um cartão."
    else:
        return "Você é menor de idade e não pode comprar o produto."

# Testes com diferentes idades e estados de cartão
idades = [18, 16, 25, 30]  # Lista com diferentes idades para testar
tem_cartao = True  # Define se a pessoa tem cartão