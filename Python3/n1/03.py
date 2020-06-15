#3 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.(2,0)
while True:
    numero = int(input("Insira um numero: "))
    if numero >= 0 and numero <= 10:
        print("Numero valido: ", numero)
        break
    else:
        print("Numero invalido. Insira novamente")
