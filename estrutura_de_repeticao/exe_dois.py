vSenha = int(input("Digite a sua senha: "))
vSenha_usuario = int(input("Digite a sua senha novamente: "))

while vSenha_usuario != vSenha:
    print("Senha inválida")
    vSenha_usuario = int(input("Digite a sua senha  novamente: "))

print("Login aceito")