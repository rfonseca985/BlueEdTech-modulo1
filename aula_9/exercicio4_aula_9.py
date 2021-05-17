#Crie um código em Python que receba uma lista de nomes informados pelo usuário com tamanho indefinido 
# (a lista deve ser encerrada quando o usuário digitar 0) e, 
# na sequência, receba um nome para que seja verificado se este consta na lista ou não. Observação: 
# ignorar diferenças entre maiúsculas e minúsculas.
def remover_repitidos(lista_nomes):
    lista = []
    if 0 not in lista_nomes:
        for i in lista_nomes:
            if i not in lista:
                lista.append(i)    
        lista.sort()
        return lista

lista_nomes = input("Digite os nomes que deseja adicionar a lista saparados por espaço  ou digite zero para encerrrar: ").upper().split(" ")
lista_nomes = remover_repitidos(lista_nomes)
print(lista_nomes)

