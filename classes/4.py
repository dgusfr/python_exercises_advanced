class contaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0.0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo    

    def alterarNome(self,nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista 
        print('\nNome alterado para: ',self.nomeCorrentista)

    def deposito(self,valor):
        self.saldo += valor
        print('\nDeposito realizado no valor de: R$',valor, '\nO saldo atual é de: R$',self.saldo)

    def saque(self,valor):
        self.saldo -= valor
        print('\nSaque realizado no valor de: R$',valor, '\nO saldo atual é de: R$',self.saldo)

#Teste Classe
conta = contaCorrente(2323232,'João', 200) 
conta.alterarNome('Jose')
conta.deposito(100)
conta.saque(10)
print('\nSaldo R$',conta.saldo)

