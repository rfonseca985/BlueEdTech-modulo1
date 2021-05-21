#Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas
#de um supermercado. Não esqueça de fazer as seguintes validações:
#estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45], "batata": [2001, 1.20],
#"feijão": [100, 1.50]}
#Produto Indisponível
#Produto Inválido
#Quantidade solicitada não disponível
#O programa deverá mostrar para o cliente a quantidade de itens comprados e o total a
#pagar.

estoque = {'arroz': [80, 16.00], 'cerveja': [200, 3.50], 'feijão': [100, 6.00], 'cebola': [60, 5.00], 'refrigerante':[92, 10.00], 'papel higiênico': [0, 30.00], 'queijo':[35, 22.00], 'cenoura':[45, 5.00], 'alface': [25, 1.50]}
saida = ''
venda = []
total = 0 

while saida != 'fim':
    produto = input("Digite o produto que desesja comprar: ").lower()
    if produto not in estoque:
        print(produto,'Produto indisponivel')
        continue
    qtd = int(input("Digite a quantidade que desesja comprar: "))
    if qtd > estoque[produto][0]:
        print('Quatidade maior que disponivel no estoque!!!')
        continue
    
    compra = produto,qtd
    venda.append(compra)
    saida = input("Enter para continuar comprando ou fim para finalizar a compra: ")

for item in venda:
    produto, quantidade = item
    preco = estoque[produto][1]
    custo = preco * quantidade
    estoque[produto][0]-= quantidade
    print('produto:',produto,'/ qtd:',quantidade ,'/ preço unt: R$ {0:.2f}'.format(preco), '/ total: R$ {0:.2f}'.format(custo))
    total += custo
print('Valor total: R$ {0:.2f}'.format(total))

