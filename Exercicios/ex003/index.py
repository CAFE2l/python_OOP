class ContaBancaria:
    # Cria uma conta bancária e permite fazer saques e depósitos 
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self. saldo = saldo
        print(f"conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")    
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")
    def saque(self, valor):
        if valor > self.saldo:
            print(f"Saque de R${valor:,.2f} recusado. Saldo insuficiente na conta {self.id}")
        else:
            self.saldo -= valor
            print(f"saque de R${valor:,.2f} autorizado na conta {self.id}")


c1 = ContaBancaria(122, "CAFÉ", 500)
c1.deposito(500)
c1.saque(6000)
print(c1)