import os

class Numero:
    
    def __init__(self, valor):
        self.valor = valor

    def verificaPositivo(self):
        if self.valor >= 0:
            return "positivo"
        else:
            return "negativo"
        
os.system("clear")

numeroInserido = int(input("Insira um número: "))
numero = Numero(numeroInserido)

print("")
print("O número inserido é:", numero.valor)
print("Ele é:", numero.verificaPositivo())
print("")