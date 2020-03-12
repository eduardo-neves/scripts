import os

class Pessoa:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def maiorDeIdade(self, age):
        if self.age >= 18:
            return "maior de 18 anos"
        else:
            return "menor de 18 anos"
            
os.system('clear')

nome = input("Insira seu nome: ")
idade = int(input("Insira a sua idade: "))
p1 = Pessoa(nome, idade)

print("")
print("Seu nome é", p1.name)
print("Sua idade é", p1.age, "anos")
print("Você é", p1.maiorDeIdade(p1.age))
print("")

