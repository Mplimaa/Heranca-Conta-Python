# Herança em Python - Sistema de Contas Bancárias 🏦🐍

Este repositório faz parte de atividades de estudo do **Curso Técnico em Desenvolvimento de Sistemas** (Educação Profissional).  
O código foi **adaptado e testado** a partir do material do curso, incluindo exemplos de saídas para melhor compreensão.

## Estrutura do Projeto

Heranca-Conta-Python/
│
├── ContaTarifas.py # Classe com métodos estáticos para cálculo de tarifas
├── ContaBancaria.py # Classe base que representa uma conta genérica
├── ContaCorrente.py # Classe derivada que representa uma conta corrente
└── ContaPoupanca.py # Classe derivada que representa uma conta poupança


## Classes e Funcionalidades

### 🔹 `CalculadoraTarifas` (em `ContaTarifas.py`)
- **Classe utilitária** com métodos estáticos para cálculo de tarifas:
  - `calcular_tarifa_base()` → tarifa fixa (ex.: R$ 5,00).
  - `calcular_tarifa_transacao(numero_transacoes)` → tarifa extra caso ultrapasse 10 transações.
  - `calcular_tarifa_saldo(saldo)` → tarifa adicional se o saldo for menor que R$ 1000.

### 🔹 `ContaBancaria` (em `ContaBancaria.py`)
- **Classe base** para contas.
- Atributos:
  - `numero_conta`, `saldo`, `numero_transacoes`.
- Métodos:
  - `depositar(valor)` → adiciona valor ao saldo e registra transação.
  - `sacar(valor)` → retira valor do saldo e registra transação.
  - `calcular_tarifa()` → usa `CalculadoraTarifas` para calcular a tarifa total.

### 🔹 `ContaCorrente` (em `ContaCorrente.py`)
- Herda de `ContaBancaria`.
- Representa contas correntes.
- Exemplo de uso no próprio arquivo.

### 🔹 `ContaPoupanca` (em `ContaPoupanca.py`)
- Herda de `ContaBancaria`.
- Representa contas poupança.
- Exemplo de uso no próprio arquivo.

---


### Criando e testando uma **Conta Corrente**:

from ContaCorrente import ContaCorrente

conta_corrente = ContaCorrente("12345")
conta_corrente.depositar(1000)
conta_corrente.sacar(200)

print("Tarifa da conta corrente:", conta_corrente.calcular_tarifa())



### Criando e testando uma **Conta ContaPoupanca**:

from ContaPoupanca import ContaPoupanca

conta_poupanca = ContaPoupanca("54321")
conta_poupanca.depositar(500)
conta_poupanca.sacar(100)

print("Tarifa da conta poupança:", conta_poupanca.calcular_tarifa())



from ContaPoupanca import ContaPoupanca

conta_poupanca = ContaPoupanca("54321")
conta_poupanca.depositar(500)
conta_poupanca.sacar(100)

print("Tarifa da conta poupança:", conta_poupanca.calcular_tarifa())



### Saída Esperada:

Tarifa da conta corrente: 5



### Exemplo ao rodar ContaPoupanca.py:

Tarifa da conta poupança: 15




### Conceitos Demonstrados

Herança de classes (ContaCorrente e ContaPoupanca herdando de ContaBancaria)
Métodos estáticos (CalculadoraTarifas)
Encapsulamento da lógica de tarifas
Exemplo didático de POO em Python




Tarifa da conta corrente: 5

