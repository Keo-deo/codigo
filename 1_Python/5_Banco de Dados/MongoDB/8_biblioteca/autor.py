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

def psq_autor(nome):
    dados = colection.find_one('nome',nome)
    return dados

def upd_autor(nome,n_nome, n_birthdate):
    psq_autor(nome)
    dados = {
        "nome": n_nome,
        "birthdate": n_birthdate 
    }
    colection.update_one({'nome':nome}, {"$set":dados}) 

def del_autor(nome):
    colection.delete_one({'nome':nome})

