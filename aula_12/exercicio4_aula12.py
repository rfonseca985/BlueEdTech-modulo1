#Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. 
# Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.
import random
from operator import itemgetter


jogadas = {}
count = 1

while count <= 4:
    jogada = random.randint(1,20)
    jogador = 'jogador' + str(count)
    jogadas.update({jogador:jogada})
    count +=1

print(jogadas)
print(sorted(jogadas.items(), key= itemgetter(1), reverse=True))

