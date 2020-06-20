#from connection import conexao

class musica:
    def __init__(self, nome, autor, genero):
        self.nome = nome
        self.autor = autor
        self.genero = genero

    def apresentarDados(self):
        print(self.autor, "-", self.nome)
        print("Gênero:", self.genero)


novaMusica = musica("Tribe 303", "Aero Chord", "Trap/Psytrance")
novaMusica.apresentarDados()



