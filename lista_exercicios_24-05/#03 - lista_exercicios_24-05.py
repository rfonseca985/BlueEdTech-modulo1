#03 - Utilizando estruturas de repetição com teste lógico, 
# faça um programa que peça uma senha para iniciar seu processamento, 
# só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
# onde o computador vai “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, 
# no final mostre quantos palpites foram necessários para vencer.
import random
i = 1
senha = 'Bluemer'
numero = random.randint(1,20)
print(numero)
tentativa = ''
palpites = []
print('Qual a senha?')
entrada = input("Digite a senha para continuar: ")
while entrada != senha:
    print("Senha inválida")
    entrada = input("Digite a senha para continuar: ")
print('\nBem vindo ao joga da adivinhação\n')
print('=='*20)
print('REGRAS')
print('=='*20)
print('\nO computador vai pensar em um número inteiro entre 0 e 20.\n E você vai tentar adivinha\n')
print('=='*20)

while tentativa != numero:
    tentativa = int(input(f'Qual seu {i}º palite? '))
    palpites.append(tentativa)
    i+=1
    print('=='*20)
    if tentativa > numero:
        print('=='*20)
        print('Seu palpite é maior que número correto :')
        print('=='*20)
    elif tentativa < numero:
        print('=='*20)
        print('Seu palpite é menor que número correto')
        print('=='*20)
    else:
        print('\no número era',numero)
        print('=='*20)
        print('\nParabéns você acertou\n')
        print('=='*20)
print('=='*20)
print('Seus palpites foram',palpites)
print('=='*20)





