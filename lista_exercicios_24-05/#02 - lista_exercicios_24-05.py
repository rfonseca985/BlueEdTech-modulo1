#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e 
# mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
a = 0
e = 0
i = 0
o = 0
u = 0
cont = 0
consoantes = ''
frase = input("Digite uma frase de sua preferência: ").lower()
 
while cont < len(frase):
    if frase[cont] == 'a':
        a =+1
        pass
    elif frase[cont] == 'e':
         e +=1
         pass
    elif frase[cont] == 'i':
         i +=1
         pass
    elif frase[cont] == 'o':
         o +=1
         pass  
    elif frase[cont] == 'u':
        u += 1
        pass
    else:
        consoantes = consoantes+ frase[cont]
    cont+=1

print('Total de A na frase', a)
print('Total de E na frase', e)  
print('Total de I na frase', i)  
print('Total de O na frase', o)  
print('Total de U na frase', u)
print(consoantes)      