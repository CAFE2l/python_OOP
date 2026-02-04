from rich.console import Console
from rich.table import Table

class Produto: 
    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco

    def etiqueta_preco(self):
        console = Console()
        tabela = Table(title="Etiqueta de Preço")

        tabela.add_column("Produto", style="cyan", justify="center")
        tabela.add_column("Preço (R$)", justify="center")
    
        tabela.add_row(self.nome, f"{self.preco:,.2f}")
q
p1 = Produto("caderno", 12.50)
p1.etiqueta_preco()