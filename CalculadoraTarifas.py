
class CalculadoraTarifas:
# @staticmethod é um decorador Método estático: não precisa de 'self' nem da criação de
# um objeto da classe, pode ser chamado diretamente pela classe, sem instância
    @staticmethod
    def calcular_tarifa_base():
        return 5 # Exemplo: tarifa base de R$ 5 para todas as contas
    
    @staticmethod
    def calcular_tarifa_transacao(numero_transacoes):
        if numero_transacoes > 10:
            return (numero_transacoes - 10) * 1.5 # Exemplo: R$ 1,50 por transação adicional
        else:
            return 0
        
    @staticmethod
    def calcular_tarifa_saldo(saldo):
        if saldo < 1000:
            return 10 # Exemplo: tarifa de R$ 10 para saldos abaixo de R$ 1000
        else:
            return 0