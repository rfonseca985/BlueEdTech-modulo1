#	Crie um código em Python para exibir a contagem de dígitos de um número inteiro positivo informado pelo usuário.
num =input("Digite um numero: ").replace('-','')
if num not in ("1234567890"):
        print(num,"não é um número")
else:
    print("O número",num,"contém",len(num),"dígitos")