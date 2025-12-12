class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None
