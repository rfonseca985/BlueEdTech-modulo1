#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".
print ("Iniciando interrregatório (responda SIM ou NÃO):")
print("=================================================")
resp1 = input("Telefonou para a vítima? ")
print("=================================================")
resp2 = input("Esteve no local do crime? ")
print("=================================================")
resp3 = input("Mora perto da vítima? ")
print("=================================================")
resp4 = input("Devia para a vítima? ")
print("=================================================")
resp5 = input("Já trabalhou com a vítima? ")
print("=================================================")
lista= [resp1.upper(), resp2.upper(), resp3.upper(), resp4.upper(), resp5.upper()]

count = lista.count("SIM") 
      
if count == 2:
    print("Resultado do interrogatório: Suspeito ")
elif count >= 3 and count <5:
    print("Resultado do interrogatório: Cumplice ")
elif count > 4:
    print("Resultado do interrogatório: Culpado!!! ")
else:
    print("Resultado do interrogatório: Inocente ")