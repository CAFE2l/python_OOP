class Gafanhoto:
    def __init__(self, n = "visitante", i=0): #metodo constructor
        #atributos da instancia
        
        self.nome = n
        self.idade = i


    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."


g1 = Gafanhoto("Fulano de tal", 20)
g1.aniversario()
print(g1.mensagem())