#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
#Os códigos utilizados são:
#1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
total_votos = 0
total_nulos = 0
total_brancos = 0
votos = ''
print("Os candidátos são 1 - Ladrão / 2 - Pilantra / 3 - Safado / 4 - Corrupto / 5 - Nulo / 6 - Branco ")
while votos != 0:
    votos = int(input("Digite o número relativo ao seu candidáto: "))
    if votos == 1:
        print("Você votou no candidáto: 1 - Ladrão")
        total_votos +=1
    elif votos == 2:
        print("Você votou no candidáto: 2 - Pilantra")
        total_votos +=1
    elif votos == 3:
        print("Você votou no candidáto: 3 - Safado")
        total_votos +=1
    elif votos == 4:
        print("Você votou no candidáto: 4 - Corrupto")
        total_votos +=1
    elif votos == 5:
        print("Você votou no candidáto: 5 - Nulo")
        total_votos +=1
        total_nulos +=1
    elif votos == 6:
        print("Você votou no candidáto: 6 - Branco")
        total_votos +=1
        total_brancos +=1

porcentagem_nulos = total_nulos/100 * total_votos
porcentagem_brancos = total_brancos/100* total_votos        
print("Total de votos:",total_votos)
print("Total de votos nulos:",total_nulos,"%")
print("Total de votos brancos:",total_brancos,"%")
print("Porcentagem de votos nulos:",porcentagem_nulos)
print("Porcentagem de votos brancos:",porcentagem_brancos)
    
    

