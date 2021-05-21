#Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
#celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
#retornar a data completa. Não esqueça de validar se a celebridade escolhida está
#presente em seu dicionário.


celebridades = {'Albert Eisntein': '14/03/1979', 'Benjamin Franklin': '17/01/1706', 'Chuck Norris': '10/03/1940', 'Donald Trump': '14/06/1946', 'Bruce Lee': '27/11/1940', 'Rowan Atkinson': '06/01/1955' }
def buscar_celebridades(key):
     print(celebridades.get(key))
       
print('Bem vindo ao nosso calendário. Sabemos a data de nascimento das seguintes celebridades: \nAlbert Eisntein \nBenjamin Franklin \nBruce Lee \nChuck Norris \nDonald Trump \nRowan Atkinson')
nome = input("Digite o nome da celebridade que deseja saber a data de nascimento: ")
while nome not in celebridades:
    print('Essa celebridade não consta em nossa lista!!!')
    print('Sabemos a data de nascimento das seguintes celebridades: \nAlbert Eisntein \nBenjamin Franklin \nBruce Lee \nChuck Norris \nDonald Trump \nRowan Atkinson')
    nome = input("Digite o nome da celebridade que deseja saber a data de nascimento: ")
buscar_celebridades(nome)


    
    
                          