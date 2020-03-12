import os

class Compra:
    
    def __init__(self, valorPago, valorProduto):
        self.valorPago = valorPago
        self.valorProduto = valorProduto

    def calculaTroco(self):
        return self.valorPago - self.valorProduto

os.system("clear")

pago = float(input("Insira o valor pago: "))
preco = float(input("Insira o preço do produto: "))
compra = Compra(pago, preco)

print("")
print("O valor pago é:", compra.valorPago)
print("O valor do produto é:", compra.valorProduto)
print("O troco é:", compra.calculaTroco())
print("")