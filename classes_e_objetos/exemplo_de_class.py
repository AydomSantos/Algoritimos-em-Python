"""
Conta Bancaria Class
"""
class ContaBancaria:
    def __init__(self, pTitular):
        self.pTitular = pTitular
        self.saldo = 0.0
        self.historico_transacoes = []
        print(f"Conta bancária criada para {self.pTitular}.")

    def depositar(self, pValor):
        if pValor > 0:
            self.saldo += pValor
            self.historico_transacoes.append(f"Depósito de R$ {pValor:.2f}")
            print(f"Depósito de R$ {pValor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, pValor):
        if pValor > 0:
            if self.saldo >= pValor:
                self.saldo -= pValor
                self.historico_transacoes.append(f"Saque de R$ {pValor:.2f}")
                print(f"Saque de R$ {pValor:.2f} realizado com sucesso.") # Adicionei esta linha para feedback
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.") # Corrigi a mensagem

    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self.pTitular}: R$ {self.saldo:.2f}")

    def exibir_extrato(self):
        print(f"\nExtrato da conta de {self.pTitular}:")
        if not self.historico_transacoes:
            print("Nenhuma transação realizada ainda.")
        else:
            for transacao in self.historico_transacoes:
                print(f"- {transacao}")
            print(f"Saldo final: R$ {self.saldo:.2f}")

"""
Conta Corrente
"""
class ContaCorrente(ContaBancaria):
    def __init__(self, pTitular, pLimite_cheque_especial):
        super().__init__(pTitular)
        self.pLimite_cheque_especial = pLimite_cheque_especial
        print(f"Conta corrente criada para {self.pTitular} com limite de cheque especial de R$ {self.pLimite_cheque_especial:.2f}.")

    def sacar(self, pValor):
        if pValor > 0:
            vSaldo_total = self.saldo + self.pLimite_cheque_especial
            if vSaldo_total >= pValor:
                self.saldo -= pValor
                self.historico_transacoes.append(f"Saque de R$ {pValor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente (incluindo cheque especial) para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        vSaldo_total = self.saldo + self.pLimite_cheque_especial
        print(
            f"Saldo atual da conta corrente de {self.pTitular}: R$ {vSaldo_total:.2f} (Limite cheque especial: R$ {self.pLimite_cheque_especial:.2f})")

"""
Conta Poupanca
"""
class ContaPoupanca(ContaBancaria):
    def __init__(self, pTitular, pTaxa_juros):
        super().__init__(pTitular)
        self.pTaxa_juros = pTaxa_juros
        print(f"Conta poupança criada para {self.pTitular} com taxa de juros de {self.pTaxa_juros * 100:.2f}% ao mês.")

    def aplicar_juros(self):
        vJuros = self.saldo * self.pTaxa_juros # Corrigi aqui: self.vTaxa_juros para self.pTaxa_juros
        self.saldo += vJuros
        self.historico_transacoes.append(f"Juros de R$ {vJuros:.2f} aplicados.")
        print(f"Juros de R$ {vJuros:.2f} aplicados na conta de {self.pTitular}.")
        self.exibir_saldo()

"""
Class Cliente
"""

class Cliente:
    def __init__(self, pNome, pCpf):
        self.pNome = pNome
        self.pCpf = pCpf
        self.contas = []
        print(f"Cliente {self.pNome} (CPF: {self.pCpf}) cadastrado.")

    def adcionar_conta(self, pConta):
        if isinstance(pConta, ContaBancaria):
           self.contas.append(pConta)
           print(f"Conta adicionada para o cliente {self.pNome}.")
        else:
            print("O objeto fornecido não é uma instância de ContaBancaria ou suas subclasses.")

    def listar_contas(self):
        print(f"\nContas do cliente {self.pNome} (CPF: {self.pCpf}):")
        if not self.contas:
            print("Nenhuma conta cadastrada para este cliente.")
        else:
            for i, conta in enumerate(self.contas):
                print(f"\n--- Conta {i + 1} ---")
                print(f"Titular: {conta.pTitular}")
                if isinstance(conta, ContaCorrente):
                    print(f"Tipo: Conta Corrente")
                    print(f"Limite Cheque Especial: R$ {conta.pLimite_cheque_especial:.2f}")

