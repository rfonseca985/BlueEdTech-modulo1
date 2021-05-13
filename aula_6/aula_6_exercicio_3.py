#Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    total = (taxaImposto/100 +1) * custo
    return print("R$ {0:.2f}".format(total))

tx = int(input("Digite a taxa do imposto:"))
cst = float(input("Digite o custo do produto:"))

somaImposto(tx, cst)

