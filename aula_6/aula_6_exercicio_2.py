#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.
def sinal(x):
    if x < 0:
        return print("O valor é: Negativo")
    else:
        return print("O valor é: Positivo")

n = int(input("Digite um valor negatico ou positivo: "))    

sinal(n)