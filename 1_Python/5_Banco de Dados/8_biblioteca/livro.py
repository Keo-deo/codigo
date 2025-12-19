from bson import ObjectId
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["biblioteca"]

colection = db["livro"]

dados = {
    "nome":"teste 3"
}

res = colection.insert_one(dados)
print(res)