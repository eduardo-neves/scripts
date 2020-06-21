from musica import Musica

nome = str(input("Insira o nome: "))
autor = str(input("Insira o autor: "))
genero = str(input("Insira o gênero: "))

musica = Musica()
musica.salvar(nome, autor, genero)
musica.listar()