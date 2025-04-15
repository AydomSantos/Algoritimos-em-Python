
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
            self.saldo -= pValor
            self.historico_transacoes.append(f"Saque de R$ {pValor:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

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
