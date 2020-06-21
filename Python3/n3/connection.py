from pymongo import MongoClient

class MongoConnect():

    def save(self, json):
        try:
            client = MongoClient('localhost', 27017)
            n3_musicas = client.n3_musicas
            musicas = n3_musicas.musicas
            id = musicas.insert_one(json).inserted_id
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)

    def listar(self):
        client = MongoClient('localhost', 27017)
        n3_musicas = client.n3_musicas
        musicas = n3_musicas.musicas
        for musica in musicas.find():
            print(musica)