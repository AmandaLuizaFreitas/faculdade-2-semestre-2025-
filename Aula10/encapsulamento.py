# encapsulamento

class ContaBancaria:                
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular          # Atributo privado
        self.__saldo = saldo_inicial      # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        return self.__saldo

    def obter_titular(self):
        return self.__titular
# Exemplo de uso
conta = ContaBancaria("João Silva", 1000)
conta.depositar(500)
conta.sacar(200)
print(f"Saldo atual: R${conta.consultar_saldo()}")
print(f"Titular da conta: {conta.obter_titular()}") 
