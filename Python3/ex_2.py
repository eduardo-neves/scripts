import os

class Numero:

    def __init__(self, numero):
        self.numero = numero
    
    def numeroExtenso(self):
            if self.numero == 1:
                return "um"
            if self.numero == 2:
                return "dois"
            if self.numero == 3:
                return "três"
            if self.numero == 4:
                return "quatro"
            if self.numero == 5:
                return "cinco"
            else:
                return "Valor inválido"
              
os.system('clear')
numero = int(input("Insira um número: "))
n1 = Numero(numero)

print("")
print("Número digitado foi:", n1.numero)
print("Resultado:", n1.numeroExtenso())
print("")
