#Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.
strg = input("Digite um texto qualquer: ")
low = strg.lower()
consoantes ='' 
for letra in low:
    if letra not in 'aeiouãõ':
        consoantes += letra

print(consoantes)