#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , 
# além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
import datetime 

dados_funcionario = {}

nome = input("\nDigite o nome do funcionário: ")
data_nasc = input("Digite o ano de nascimento (dd/MM/yyyy): ")
dtn= datetime.datetime.strptime(data_nasc, "%d/%m/%Y")
ctps = input("Digite o número da carteira de trabalho: ")
idade= datetime.datetime.now().year - dtn.year
dados_funcionario[ctps]= nome
dados_funcionario['data de nascimento'] = data_nasc
dados_funcionario['idade'] = idade
if ctps != 0:
    data_contrat  = input("Digite o ano de contratação (dd/MM/yyyy):")
    dtc= datetime.datetime.strptime(data_contrat, "%d/%m/%Y")
    aposentadoria =   (dtc.year - dtc.year) + 35 + idade
    salario = input("Digite o salário:")
    dados_funcionario['ano da contratação']= data_contrat
    dados_funcionario['salário']= salario
    dados_funcionario['previsão da aposentadoria']= aposentadoria
print(dados_funcionario)