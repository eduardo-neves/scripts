def verificaMaior(n1, n2):
    if n1 > n2:
        return "O primeiro número é maior"
    if n1 < n2:
        return "O segundo número é maior"
    if n1 == n2:
        return "Número iguais"

primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))

print(verificaMaior(primeiroNumero, segundoNumero))
