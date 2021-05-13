#Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.
def compara_num(n1,n2):
    if n1 == n2:
        print(n1,n2,"São iguais!!!")
    elif n1 < n2:
        print(n1,"É menor que", n2)
    else:
        print(n2,"É menor que", n1)

num1 = input("Digite o primeiro caracter: ")
num2 = input("Digite o segundo caracter: ")

compara_num(num1, num2)