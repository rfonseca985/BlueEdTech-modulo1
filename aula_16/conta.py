class conta():
    def __init__(self,titular, saldo):
         self.titular = titular
         self.saldo = saldo


    def depositar(self,valor_deposito):
        self.saldo = self.saldo + valor_deposito

    
    def sacar(self, valor_saque):
        if valor_saque > self.saldo:
            print('saldo insuficiente')
        else:
            self.saldo = self.saldo - valor_saque


titular = input('Digite o nome do titular da conta: ')
saldo = float(input('Digite o valor do saldo inicial da conta: '))
conta1 = conta(titular, saldo)
print('Nome do titular: {}, seu saldo é: R${:0.2f}'.format(conta1.titular, conta1.saldo))

deposito = float(input('Quanto deseja depositar: '))
conta1.depositar(deposito)
print('Depósito efetuado no valor de: R${:0.2f}, seu saldo atualizado é: R${:0.2f}'.format(deposito, conta1.saldo))

saque = float(input('Quanto deseja sacar: '))
conta1.sacar(saque)
print('Saque no valor de: R${:0.2f} efetuado com sucesso, seu saldo atualizado é: R${:0.2f}'.format(saque, conta1.saldo))


    