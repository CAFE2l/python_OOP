
from rich import print
class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return (f"Olá, me chamo {self.nome} e trabalho no setor de {self.setor} atuando como {self.cargo}")

g1 = Funcionario("CAFE", "TI", "desenvolvedor")
print(f":handshake: {g1}")