from connection import MongoConnect

class Musica():

    def salvar(self, nome, autor, genero):
        connection = MongoConnect()
        musica = {'nome': nome, 'autor': autor, 'genero': genero}
        connection.save(musica)

    def listar(self):
        connection = MongoConnect()
        connection.listar()
