#Faça um programa que leia dez conjuntos de dois valores, 
# o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.  
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

num_aluno = []
altura_aluno = []
n_aluno = 1
numero = True

while num_aluno != 10:
    print("\nAluno n° ", n_aluno)
    numero = int(input("Digite o numero do aluno: "))
    if numero == 0:
        break
    else:
        altura = float(input("Digite a altura: "))
        
        num_aluno.append(numero)
        altura_aluno.append(altura)
        n_aluno += 1


num_alto = altura_aluno.index(max(altura_aluno))
num_baixo = altura_aluno.index(min(altura_aluno))
print()
print("Número do mais alto: ", num_aluno[num_alto],"medindo:",max("{0:.2f}".format(altura_aluno)))
print("Número do mais baixo: ", num_aluno[num_baixo],"medindo:",min("{0:.2f}".format(altura_aluno)))

