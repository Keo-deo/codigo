from bson import ObjectId
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["biblioteca"]

colection = db["autor"]

dados = {
    "nome":"teste 0"
}

res = colection.insert_one(dados)
print(res)


def add_autor(nome,birthdate):
    dados = {
        "nome": nome,
        "birthdate": birthdate 
    }
    author = colection.insert_one(dados)
    return author

def ex_autor():
    dados = colection.find()
    return dados

def psq_autor():
    obj = ObjectId(id)
    dados = colection.find_one('_id', ObjectId)
    return dados