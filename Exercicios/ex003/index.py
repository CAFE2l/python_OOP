class ContaBancaria:
    # Cria uma conta bancária e permite fazer saques e depósitos 
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self. saldo = saldo
    
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor



c1 = ContaBancaria(122, "CAFÉ", 500)
c1.deposito(500)
c1.saque(600)
print(c1)