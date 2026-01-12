class Gafanhoto: 
    def __init__(self):
        self.nome = ''
        self.idade = 0


    def aniversario(self):
        self.idade += 1;

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


g1 = Gafanhoto()
g1.nome = "CAFÉ"
g1.idade = 16
g1.aniversario()


g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53

print(g2.mensagem())