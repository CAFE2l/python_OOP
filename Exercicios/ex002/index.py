
class Gafanhoto:


    def __init__(self, nome = "visitante", idade=0): #metodo constructor        #atributos da instancia        
        self.nome = nome
        self.idade = idade


    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"



g1 = Gafanhoto("Fulano de tal", 20)
g1.aniversario()
print(g1)

print(g1.__doc__) #Dunder Attribute
print(g1.__dict__)# Attribute
print(g1.__getstate__()) #Method
print(g1.__class__)


