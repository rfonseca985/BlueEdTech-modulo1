# Desenvolva um código em Python que gere um número aleatório de 1 a 100 e dê ao usuário 10 chances para acertá-lo. 
# A cada tentativa, deve ser impressa a quantidade de tentativas restantes e se o número aleatório é maior ou menor do que o número inserido na tentativa atual. 
# Se o usuário não acertar em 10 tentativas, informe qual o número aleatório. [Dica: use a função randint para gerar o número aleatório]
import random
numero = random.randrange(100)
print(numero)
chances = 10
print("Voce tem 10 chances para advinhar o número!!!")
palpite=0

while  palpite != numero:
    palpite = int(input("\nDigite seu palite: "))
    if palpite == numero:
        print('Você venceu!!!')
    elif chances == 1 :
        print("Game over, o numero era:",numero)
        break
    elif palpite > 100:
        print("Número inválido. Você deve digitar um numero de 1 a 100. Tente novamente:")
        continue
    else:
        print("Você errou. Tente novamente")   
        chances -=1
        print("Chances:",chances)
    
        