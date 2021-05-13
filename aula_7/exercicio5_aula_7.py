#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome_jogador=" ", gols_marcados='' ):
    print("Nome do jogador:",nome_jogador,"/","Gols marcado:", gols_marcados)

nj = input("Digite o nome do jogador: ")
gm = int(input("Digite os gols marcados: "))
ficha(nj, gm) 
