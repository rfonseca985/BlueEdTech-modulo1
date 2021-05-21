#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. 
# Se não, mostre que a multiplicação não foi maior que 40.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1+ num2 
multiplicacao = num1 * num2
divisao = num1// num2

print('\nResultado da soma:',soma,'\n')
print("=="*20)
print('\nResultado da multiplicação:',multiplicacao,'\n')
print("=="*20)
print('\nResultado da divisão inteira:',divisao,'\n')
print("=="*20)

if num1 > num2:
    print('\nO número',num1, 'é o maior\n')
    print("=="*20)
else:
    print('\nO número',num2, 'é o maior\n')
    print("=="*20)

if soma%2 == 0:
    print('\nO resultado da soma é',soma, 'que um número par\n')
    print("=="*20)
else:
    print('\nO resultado da soma é',soma, 'que um número ímpar\n')
    print("=="*20)


if multiplicacao > 40 and divisao != 0:
    print('\nResultado da multiplicação dividido resusltado da divisão:',multiplicacao / divisao,'\n')
    print("=="*20)
elif divisao == 0:
    print('\nResultado da multiplicação dividido resusltado da divisão:',divisao,'\n')
    print("=="*20)
else:
    print('\n',multiplicacao, 'não é maior que 40\n')
    print("=="*20)

