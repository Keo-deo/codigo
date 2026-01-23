from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["tranferencia_de_jogadores"]

colection = db["jogadores"]

def ad_jogador(nome, preco):
    dados_jogador = {
        "nome": nome,
        "preco": preco
    }

    res = colection.insert_one(dados_jogador)