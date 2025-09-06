from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        super().__init__(numero_conta, saldo, numero_transacoes)

if __name__ == "__main__":
    conta_corrente = ContaCorrente("12345")
    conta_corrente.depositar(1000)
    conta_corrente.sacar(200)
    print("Tarifa da conta corrente:", conta_corrente.calcular_tarifa())