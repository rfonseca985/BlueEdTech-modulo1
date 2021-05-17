#Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em dois números de dois algarismos que somados e 
# elevando-se a soma ao quadrado obtenha-se o próprio número.
for x in range(1000,10000):
    n1 = x // 100
    n2 = x % 100
    if(n1+n2)**2 == x:
        print(x)