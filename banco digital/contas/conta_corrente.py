from contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, numero_conta, saldo=0, limite=500):
        super().__init__(cliente, numero_conta, saldo)
        self.limite = limite 

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Limite insuficiente!")
            return False
        
        self.saldo -= valor
        return super().sacar(0)  

    def __str__(self):
        return f"Conta Corrente {self.numero_conta} | Cliente: {self.cliente} | Saldo: {self.saldo} | Limite: {self.limite}"
