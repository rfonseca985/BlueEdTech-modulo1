# Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece uma vogal.
strg = input("Digite um texto qualquer: ")
low = strg.lower() 
a = low.count("a")
e = low.count("e")
i = low.count("i")
o = low.count("o")
u = low.count("u")
vogais = a + e + i + o + u 
print(vogais)