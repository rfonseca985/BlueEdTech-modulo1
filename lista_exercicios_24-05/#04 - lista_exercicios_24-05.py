#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato D de mesPorExtenso de AAAA. Valide a data e retorne NULL caso a data seja inválida.
import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'pt_BR')

def data_extenso(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        print("Formata inválido")
        return None
    else:
        data_t = datetime.strptime(data, '%d/%m/%Y')
        return  datetime.strftime(data_t," %d de %B de %Y")

data = input('Digite uma data no formato (dd/MM/yyyy): ')
d_final =  data_extenso(data)
if data_extenso is not None:
    print('Dia',d_final)

    