#2 - Crie um classe Funcionário com os atributos nome, idade e salário. 
#Deve ter  um método aumenta_salario. Crie duas subclasses da classe funcionário,
# programador  e analista, implementando o método nas duas subclasses. 
# Para o programador some ao atributo salário mais 20 e ao analista some ao salário mais 30,  
# mostrando na tela o valor. Depois disso, crie uma classe de testes instanciando os
#  objetos programador e analista e chame o método aumenta_salario de cada um.(2,0)

class funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumenta_salario(self):
        self.salario = self.salario + self.aumento

class programador(funcionario):
    def __init__(self, nome, idade, salario):
        funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20

class analista(funcionario):
    def __init__(self, nome, idade, salario):
        funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30

p1 = programador("Eduardo", 20, 1000)
print(p1.nome)
print(p1.salario)
p1.aumenta_salario()
print(p1.salario)

a1 = analista("João", 18, 1500)
print(a1.nome)
print(a1.salario)
a1.aumenta_salario()
print(a1.salario)