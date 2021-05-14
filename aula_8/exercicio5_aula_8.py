#Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores. 
# Caso seja um número primo, o programa ainda deve informar que se trata de um número primo! 
num=(int)(input("Digite um numero: "))
x= 0
for i in range(2,num):
    if(num % i == 0):
        print(i)
        x += 1
if x==0:
    print(num,"É numero primo")

