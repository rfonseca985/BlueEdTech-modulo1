#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
n_pares = []
n_impares = []

for i in range(1,8):
    num = int(input(f'Digite o {i}º numero: '))
    if num%2 == 0:
        n_pares.append(num)
    else:
        n_impares.append(num)

print(sorted('Números pares: ',n_pares))
print(sorted('Números ímpares',n_impares))