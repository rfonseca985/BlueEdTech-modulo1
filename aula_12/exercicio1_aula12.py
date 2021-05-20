#Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
# (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
#{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}
numeros = {}
numero = [1,4,5,7,9]
for i in range(len(numero)):
    n_quadrado = numero[i] * numero[i]
    numeros.update({numero[i]:n_quadrado})

print(numeros)