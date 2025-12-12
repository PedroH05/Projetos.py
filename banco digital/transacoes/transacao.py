from datetime import datetime

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now()
    
    def __str__(self):
        return f"O {self.tipo} de {self.valor} em {self.data}."
    
    
    
    
    
    
    