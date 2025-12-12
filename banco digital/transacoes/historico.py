class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append(transacao)

    def listar(self):
        for t in self.transacoes:
            print(t)
