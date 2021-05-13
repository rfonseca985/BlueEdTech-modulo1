# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.
import datetime


def data(ano=1995, mes=5, dia=2):
    x = datetime.datetime(ano, mes, dia)
    d = x.strftime("%d")
    m = x.strftime("%B")
    a = x.strftime("%Y")
    print(d, m, a)


d = int(input("Digite o dia: "))
m = int(input("Digite mês: "))
a = int(input("Digite o ano: "))


data(a, m, d)
