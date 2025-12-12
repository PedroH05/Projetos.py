class Conta:
    def __init__(self, cliente, numero_conta, saldo=0):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor < 0:
            print("Valor inválido")
            return False

        self.saldo += valor
        if valor > 0:
            self.historico.append(f"Depósito: +{valor}")
        return True

    def sacar(self, valor):
        if valor < 0:
            print("Valor inválido")
            return False

        if valor > 0:
            if valor > self.saldo:
                print("Saldo insuficiente!")
                return False
            
            self.saldo -= valor
            self.historico.append(f"Saque: -{valor}")
            return True

        return True

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Valor inválido")
            return False

        if not self.sacar(valor):
            return False

        conta_destino.depositar(valor)
        self.historico.append(f"Transferência enviada: -{valor} para conta {conta_destino.numero_conta}")
        conta_destino.historico.append(f"Transferência recebida: +{valor} da conta {self.numero_conta}")

        return True

    def exibir_extrato(self):
        for item in self.historico:
            print(item)
