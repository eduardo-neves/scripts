def calculaVolume(comprimento, altura, largura):
    volume = float
    volume = comprimento * largura * altura
    return "Volume total é:", volume

comprimento = float(input("Insira o comprimento da caixa: "))
altura = float(input("Insira a altura da caixa: "))
largura = float(input("Insira o largura da caixa: "))

print(calculaVolume(comprimento, altura, largura))

