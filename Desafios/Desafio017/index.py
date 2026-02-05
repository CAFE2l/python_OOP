from rich.console import Console
from rich.table import Table


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

def mostrar_etiquetas(produtos):
    console = Console()
    tabela = Table(title="Lista de produtos")

    tabela.add_column("Prroduto", justify="center")
    tabela.add_column("Preço", justify="center")

    for p in produtos:
        tabela.add_row(p.nome, str(p.preco))

    console.print(tabela)

p1 = Produto("Caderno", 12.50)
p2 = Produto("Lapis", 3.75)

produtos = [p1, p2]
mostrar_etiquetas(produtos)