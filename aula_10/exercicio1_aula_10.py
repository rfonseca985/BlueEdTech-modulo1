# 1 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha.

senha = int(input("Digite sua senha: "))
x = "1234567"
while x != senha :
    print("Senha incorreta, tente novamente") 
    senha = input("Digite sua senha: ")