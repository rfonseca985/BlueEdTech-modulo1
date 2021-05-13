#Escreva uma função que recebe dois números (a e b) 
# como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.
def limit(a, b):
    limite = 20
    if a + b > limite:
        return print(True)

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
limit(a,b)