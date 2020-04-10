soma = 0
nomeAluno = input("Insira o nome do Aluno: ")
for i in range(3):
    nota = float(input("Insira nota: "))
    soma += nota
media = soma / 3
def verificaAprovado():
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
print("Média é:", media)
print(verificaAprovado())
