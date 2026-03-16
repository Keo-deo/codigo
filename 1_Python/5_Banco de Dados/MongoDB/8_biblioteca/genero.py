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
    return 

def psq_genero(nome):
    dados = colection.find_one('nome',nome)
    return dados

def upd_genero(nome,n_nome):
    psq_genero(nome)
    dados = {
        "nome": n_nome,
    }
    colection.update_one({'nome':nome}, {"$set":dados}) 

def del_genero(nome):
    colection.delete_one({'nome':nome})

