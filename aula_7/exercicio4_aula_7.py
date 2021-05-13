#Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. 
#Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.
from datetime import date

def voto(dia,mes,ano):
    data_atual = date.today().year
    data_nasc = date( ano, mes, dia)
    calc_idd = data_atual - data_nasc.year
    idade = calc_idd

    if idade < 16:
        print("Voto NEGADO")
    elif idade >=16 and idade <18 or idade >=70:
        print("Voto OPCIONAL")
    else:
        print("Voto OBRIGATORIO")

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mes do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))
voto(dia, mes, ano)


