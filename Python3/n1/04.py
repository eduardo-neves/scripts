#4 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:(2,0)

numero = int(input("Insira o numero da tabuada: "))

"""def tabuada(n):
    print("Tabuada de ", n, ":\n"
        ,n, "X 1 =", n*1, "\n"
        ,n, "X 2 =", n*2, "\n"
        ,n, "X 3 =", n*3, "\n"
        ,n, "X 4 =", n*4, "\n"
        ,n, "X 5 =", n*5, "\n"
        ,n, "X 6 =", n*6, "\n"
        ,n, "X 7 =", n*7, "\n"
        ,n, "X 8 =", n*8, "\n"
        ,n, "X 9 =", n*9, "\n"
        ,n, "X 10 =", n*10, "\n"
        )
"""

def tabuada(n):
    print("Tabuada de", n, ":")
    for i in range(1,11):
        print(n,"X", i, "=", n*i)

tabuada(numero)
