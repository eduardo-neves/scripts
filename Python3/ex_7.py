import os

class Numeros:
    
    def __init__(self, valorAtual):
        self.valorAtual = valorAtual
        self.maior = maior
        self.menor = menor
        self.soma = soma
        self.media = media

    def verificaMaior(self):
        if self.valor >= 0:
            return "positivo"
        else:
            return "negativo"

    def verificaMenor(self):
        if self.valor >= 0:
            return "positivo"
        else:
            return "negativo"

os.system("clear")
numeroInserido = int(input("Insira um número: "))
numero = Numero(numeroInserido)

print("")
print("O número inserido é:", numero.valor)
print("Ele é:", numero.verificaPositivo(), numero.parOuImpar())
print("")