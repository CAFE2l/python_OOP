from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preço")

tabela.add_column("Nome", justify="center", style="red")
tabela.add_column("Preços", justify="center", style="blue")

tabela.add_row("lapis", "1.50")
tabela.add_row("borracha", "2.00")

print(tabela)
