import os

class Calculadora:

    def __init__(self, primeiroNumero, segundoNumero):
        self.primeiroNumero = primeiroNumero
        self.segundoNumero = segundoNumero
    
    def soma(self):
        return self.primeiroNumero + self.segundoNumero 
    def subtracao(self):
        return self.primeiroNumero - self.segundoNumero
    def multiplicacao(self):
        return self.primeiroNumero * self.segundoNumero
    def divisao(self):
        return self.primeiroNumero / self.segundoNumero

os.system('clear')

numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
calculo = Calculadora(numero1, numero2)

print("")
print("Soma:", calculo.soma())
print("Subtração:", calculo.subtracao())
print("Multiplicação:", calculo.multiplicacao())
print("Divisão:", calculo.divisao())
print("")


