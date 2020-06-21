from operacoes import Operacoes

op = Operacoes()
nome = str(input("Insira o nome: "))
autor = str(input("Insira o autor: "))
genero = str(input("Insira o gênero: "))
op.salvar(nome, autor, genero)
op.buscar()