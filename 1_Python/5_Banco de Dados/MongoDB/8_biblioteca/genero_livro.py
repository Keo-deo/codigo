from bson import ObjectId
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["biblioteca"]

colection = db["genero_livro"]

dados = {
    "nome":"teste 1"
}

res = colection.insert_one(dados)
print(res)