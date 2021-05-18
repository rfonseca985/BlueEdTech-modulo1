#Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois. Enquanto a soma não for 50, 
# ele deve continuar repetindo.
print("Digite 2 número que a soma de resultado igual a 50")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
if soma ==50:
    print("Muito bem",num1,"+",num2,"é igual a 50")
else:
    print("O resultado não é 50!!!")
    print("Tente novamente:")
    print("Digite 2 número que a soma de resultado igual a 50")
    while soma != 50:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        if soma ==50:
            print("Muito bem",num1,"+",num2,"é igual a 50")
            break
        else:
            print("O resultado não é 50!!!")
            print("Tente novamente:")
            print("Digite 2 número que a soma de resultado igual a 50")