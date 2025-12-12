from contas.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cliente, numero_conta, saldo=0):
        super().__init__(cliente, numero_conta, saldo)

    def sacar(self, valor):
        if valor > self.saldo:
            print("Conta Poupança não permite saldo negativo.")
            return False
        
        return super().sacar(valor)

    def __str__(self):
        return f"Conta Poupança {self.numero_conta} | Cliente: {self.cliente} | Saldo: {self.saldo}"
