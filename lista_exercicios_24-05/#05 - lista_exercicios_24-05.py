#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def consoantes(frase):
    consoantes = ''
    a = 0 
    e = 0 
    i = 0 
    o = 0
    u = 0
    cont = 0
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
    
    print('\nTotal de A na frase:', a)
    print("=="*20)
    print('Total de E na frase:', e)
    print("=="*20)  
    print('Total de I na frase:', i)
    print("=="*20)  
    print('Total de O na frase:', o)
    print("=="*20)  
    print('Total de U na frase:', u)
    print("=="*20)
    print(consoantes)
    print("=="*20)
    print('Total de letras retiradas:',a + e + i + o +u)
    print("=="*20)     

frase = input("Digite uma frase de sua preferência: ").lower()
print("=="*20)  
consoantes('Frase sem vogais:',frase)