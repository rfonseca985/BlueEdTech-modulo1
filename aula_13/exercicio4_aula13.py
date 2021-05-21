#Uma escola te contratou para desenvolver um programa em Python para que o
#professor gerencie as notas de seus alunos. Seu programa deve apresentar o seguinte
#menu:
#0. Sair
#1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
#2. Inserir aluno e nota
#3. Alterar a nota de um aluno
#4. Consultar nota de um aluno específico
#5. Apagar um aluno da lista
#6. Exibir a média da turma
#As notas e os nomes dos alunos serão fornecidos pelo professor. Implemente a sua
#solução utilizando dicionário.
import time
opcao = ''
alunos ={}
while opcao != 0:
    print('Menu')
    print('0. Sair')
    print('1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)')
    print('2. Inserir aluno e nota')
    print('3. Alterar a nota de um aluno')
    print('4. Consultar nota de um aluno específico')
    print('5. Apagar um aluno da lista')
    print('6. Exibir a média da turma')
    opcao = int(input('\nEscolha uma das opções: \n'))
    if opcao == 1:
        print(alunos)
    elif opcao == 2:
        nome = input('Nome do aluno: ')
        nota = float(input('Notas do aluno: '))
        alunos[nome] = nota
    elif opcao == 3:
        nome = input('Nome do aluno: ')
        nota = float(input('Notas do aluno: '))
        alunos.update({nome: nota})
    elif opcao == 4:
        nome = input('Nome do aluno: ')
        print(alunos.get(nome))
    elif opcao == 5:
        nome = input('Nome do aluno que deseja apagar: ')
        print('Nota:',alunos.get(nome), 'apagado com sucesso')
        del alunos[nome]
    elif opcao == 6:
       media = sum(alunos.values())/len(alunos)
       print('Média da turma {0:.1f}'.format(media))



