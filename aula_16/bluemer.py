class bluemer():
    def __init__(self,nome, sobrenome, idade):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.idade = idade
    
    def mostar_dados(self):
        print(self.nome, self.sobrenome,self.idade)



bluemer1 = bluemer('Rafael', 'Fonseca', 35)
bluemer1.mostar_dados()