#PROJETO: Gastos com viagem 
# Escrever uma aplicação utilizando funções que calcule os gastos com passagem, 
# hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.
#=======================================================================================================================================
#Hospedagem
#1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, 
# sendo que 1 noite custa R$ 140,00.
#=======================================================================================================================================

def custo_hotel(noites):
    custo_total_h = noites * 140.00
    return custo_total_h

# hotel = int(input("Digita o numero de noites da hospedagem: "))
# print("Valor total da hospendagem: R${0:.2f}".format(custo_hotel(hotel)))

#=======================================================================================================================================
#Passagem
#2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
#- São Paulo custa R$ 312,00;
#- Porto Alegre custa R$ 447,00;
#- Recife custa R$ 831,00;
#- Manaus custa R$ 986,00.
#=======================================================================================================================================

def custo_aviao(cidade):

    if cidade == "sao_paulo":
        passagem = 312.00
        return passagem
    elif cidade == "porto_alegre":
        passagem = 447.00
        return passagem
    elif cidade == "recife":
        passagem = 831.00
        return passagem
    elif cidade == "manaus":
        passagem = 986.00
        return passagem
    else:
        return print("Destino inválido")

# destino = (input("Digite seu destino: "))
# valid = destino.lower().replace('ã', 'a').replace(' ', '_')
# print("Valor da passagem: R${0:.2f}".format(custo_aviao(valid)))

#=======================================================================================================================================
#Aluguel de Carro
#3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
#- Calcule o custo do aluguel do carro sendo que:
#- A cada dia o carro custa R$ 40,00;
#- Alugando 7 dias ou +: R$ 50,00 de desconto;
#- Alugando 3 dias ou +: R$ 20,00 de desconto;
#- Você pode receber apenas um desconto;
#- Retorne o custo.
#=======================================================================================================================================

def custo_carro(dias):
    custo_diario = 40.00
    if dias >= 3 and dias < 7:
        custo_total_c = custo_diario * dias - 20.00
        return custo_total_c
    elif dias >= 7:
        custo_total_c = custo_diario * dias - 50.00
        return custo_total_c
    else:
        custo_total_c = custo_diario * dias
        return custo_total_c

# locacao = int(input("Digite quantos dias deseja locar nosso veículo: "))
# print("Valor total da locação: R${0:.2f}".format(custo_carro(locacao)))

#=======================================================================================================================================
#Cálculo Total
#4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
#- Reutilize as funções já criadas.
#- Exiba o total da viagem chamando apenas a nova função declarada!
#=======================================================================================================================================

def total_viagem(cidade, dias):
    total_hotel = custo_hotel(dias)
    total_aviao = custo_aviao(cidade)
    total_carro = custo_carro(dias)
    total = total_hotel + total_aviao + total_carro
    return total

# '''viagem_cidade = input("Escolha qual o destino da sua viagem: ")
# valid = viagem_cidade.lower().replace('ã', 'a').replace(' ', '_')
# viagem_dias = int(input("Quantos dias deseja viajar: "))
# print("Total de despesas com a viagem: R${0:.2f}".format(total_viagem(valid, viagem_dias)))

#=======================================================================================================================================
#Gastos Extras
#5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
#Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.
#=======================================================================================================================================

def gastos_extra(cidade, dias, gastos_extras):
    
    total_hotel = custo_hotel(dias)
    total_aviao = custo_aviao(cidade)
    total_carro = custo_carro(dias)
    extras = gastos_extras
    total_gastos_extras = total_hotel + total_aviao + total_carro + extras
    return total_gastos_extras


viagem_cidade = input("Escolha qual o destino da sua viagem: ")
valid = viagem_cidade.lower().replace('ã', 'a').replace(' ', '_')
viagem_dias = int(input("Quantos dias deseja viajar: ")) 
gastos_ = float(input("Gastos extras: R$ "))



print("Total de despesas com a viagem: R${0:.2f}".format(gastos_extra(valid, viagem_dias, gastos_)))