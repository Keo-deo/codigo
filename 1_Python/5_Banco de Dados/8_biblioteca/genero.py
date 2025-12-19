from bson import ObjectId
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["biblioteca"]

colection = db["genero"]

dados = {
    "nome":"teste 2"
}

res = colection.insert_one(dados)
print(res)

def add_genero(nome):
    dados = {
        "nome": nome
    }

def ex_genero():
    dados = colection.find()
    return dados