# Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def nota(nota):
    if nota < 6.0:
        print("Nota: F")
    elif nota >= 6.0 and nota < 7.0:
        print("Nota: D")
    elif nota >= 7.0 and nota < 8.0:
        print("Nota: C")
    elif nota >= 8.0 and nota < 9.0:
        print("Nota: B")
    else:
        print("Nota: A")

nt = float(input("Digite a nota do aluno: "))
nota(nt)
