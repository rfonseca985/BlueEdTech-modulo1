#Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. Se eles forem iguais, imprima que são valores idênticos.
def igualdade(n1,n2):
    if n1 < n2:
        print(n1,"É o menor")
    elif n1 == n2:
        print("Os valores são idênticos")
    else:
        print(n2,"É o menor")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite os segundo numero: "))
igualdade(num1,num2)