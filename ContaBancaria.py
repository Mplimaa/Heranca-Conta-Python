from CalculadoraTarifas import CalculadoraTarifas
from ContaBancaria import ContaBancaria

class ContaBancaria:
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.numero_transacoes = numero_transacoes
        def depositar(self, valor):
            self.saldo += valor
            self.numero_transacoes += 1

    def sacar(self, valor):
        self.saldo -= valor
        self.numero_transacoes += 1

    def calcular_tarifa(self):
        tarifa_base = CalculadoraTarifas.calcular_tarifa_base()
        tarifa_transacao = CalculadoraTarifas.calcular_tarifa_transacao(self.numero_transacoes)
        tarifa_saldo = CalculadoraTarifas.calcular_tarifa_saldo(self.saldo)
        return tarifa_base + tarifa_transacao + tarifa_saldo
    
    if __name__ == "__main__":
            conta = ContaBancaria("12345", saldo=1000)

            conta.depositar(200)
            conta.sacar(150)
            conta.depositar(50)

            print(f"Número da conta: {conta.numero_conta}")
            print(f"Saldo atual: R${conta.saldo}")
            print(f"Número de transações: {conta.numero_transacoes}")

            tarifa_total = conta.calcular_tarifa()
            print(f"Tarifa total a ser cobrada: R${tarifa_total}")