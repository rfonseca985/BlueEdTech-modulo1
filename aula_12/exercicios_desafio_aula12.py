'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, 
e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.'''
from typing import TextIO, overload
idades = []
acima = []
mulheres = []
lista_final = []
media = ''
parada = ''
while parada != 'não':
    nome = input('\nDigite seu nome:')
    sexo = input('Digite seu sexo (M ou F):').upper()
    if sexo == 'M' or sexo == 'F':
        idade = int(input('Digite sua idade: '))

    else:
        print('Sexo inválido!!!')
        sexo= input('Digite seu sexo (M ou F):')
    if sexo == 'F':
        mulheres.append(nome)
    parada = input('Deseja continuar? (sim ou não)')
    if parada == 'sim' or parada == 'não': 
        dic ={'nome': nome, 'sexo': sexo, 'idade': idade }
        idades.append(dic.get('idade'))
        media = sum(idades)/ len(idades)
        if idade > media:
            acima.append([nome, idade])
        lista_final.append(dic)
    else:
        parada = input('Deseja continuar? (sim ou não)')
        media = sum(idades)/ len(idades)
        lista_final.append({'nome': nome, 'sexo': sexo, 'idade': idade })
        idades.append(dic.get('idade'))
        media = sum(idades)/ len(idades)
        if idade > media:
            acima.append([nome,idade])
        lista_final.append(dic)
      
print(f'A lista tem {len(lista_final)} pessoas cadastradas')
print('A média de idade é {0:.2f}'.format(media))
print(f'{mulheres} são mulheres')
print(f'{acima} tem idade acima da média')
