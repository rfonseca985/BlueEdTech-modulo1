#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo sa estrutura na tela. A média para aprovação é 7. 
# Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.
resultado_final = {}
n_aluno = 1
nome = True

saida = int(input("Digite o numero de alunos:"))
for i in range(saida):
    print("\nAluno n° ", n_aluno)
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
       
    if media >= 7.0:
        resultado='APROVADO'
    elif media == 5.0 and media < 7.0:
        resultado='RECUPERAÇÃO'
    else:
        resultado='REPROVADO'

    resultado_final.update({n_aluno:[nome, media, resultado]})
    n_aluno += 1

print(resultado_final)