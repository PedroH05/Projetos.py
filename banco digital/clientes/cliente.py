class Cliente:
    def __init__ (self, nome, cpf, endereco):
        self.nome = nome 
        self.cpf = cpf 
        self.endereco = endereco
        
    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf} - {self.endereco})"
    
    