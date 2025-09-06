from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        super().__init__(numero_conta, saldo, numero_transacoes)

if __name__ == "__main__":
    conta_poupanca = ContaPoupanca("54321")
    conta_poupanca.depositar(500)
    conta_poupanca.sacar(100)
    print("Tarifa da conta poupança:", conta_poupanca.calcular_tarifa())