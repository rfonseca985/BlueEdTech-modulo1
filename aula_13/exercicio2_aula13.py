#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
#programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
#quantidade de gols feito em cada partida. No final tudo isso será guardado em um
#dicionário, incluindo o total de gols feitos durante o campeonato.


saida =''
gols = []
jogadores = {}
while saida != 'sair':
    jogadores['nome'] = input('Nome do jogador: ')
    n_partidas  =  int(input('Quantas partidas ele jogou: '))
    for i in range(1,n_partidas+1):
        gols_partida = int(input(f'Quantos gols na {i}ª patida: '))
        gols.append(gols_partida)
    
    jogadores['gols'] = sum(gols)
    print(f"O jogador {jogadores['nome']} jogou {n_partidas} marcou {gols_partida} e total de {jogadores['gols']}")  
    saida = input('Digite sair para encerrar ou enter para continuar:')

