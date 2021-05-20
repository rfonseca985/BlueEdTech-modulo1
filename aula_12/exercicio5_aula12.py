#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
import datetime 

dados_funcionario = {}
parada = True

while parada != 'sair':
    nome = input("\nDigite o nome do funcionário: ")
    data_nasc = input("Digite o ano de nascimento (dd/MM/yy): ")
    dt= datetime.datetime.strptime(data_nasc, "%d/%m/%y")
    ctps = input("Digite o número da carteira de trabalho: ")
    idade= datetime.datetime.now().year - dt.year
    dados_funcionario.update({'nome': nome, 'data de nascimento': data_nasc, 'idade': idade})
    if ctps != 0:
        data_contrat  = input("Digite o ano de contratação (dd/MM/yy):")
        dt= datetime.datetime.strptime(data_contrat, "%d/%m/%y")
        aposentadoria = dt.year + 35
        salario = input("Digite o salário:")
        dados_funcionario.update({'ano da contratação': data_contrat, 'salário': salario, 'previsão da aposentadoria':aposentadoria})
    parada = input('Digite enter para outro funcionário ou digite sair para encerrar:').lower()
print(dados_funcionario)



