from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["too_do"]

collection = db["pendencias"]

dados_pendencias = [
{ "pendencia": "Estudar MongoDB", 'status': 'pendente'}
]

def adicionar(pendencia):
    nova_pendencia = {
        "pendencia": pendencia,
        'status': 'pendente'
    }
    res = collection.insert_one(nova_pendencia)
    print(res)

def exibir():
    for doc in collection.find():
        print(doc)

def localizar(pendencia):
    item = collection.find_one({"pendencia": pendencia})
    print('se aparecer "none" significa que a pendencia nao existe!')
    print(item)
    return item

def alterar(pendencia):
    n_dados = {
        "status": "concluido",
    }
    collection.update_one({"pendencia": pendencia}, {"$set": n_dados})

def deletar(pendencia):
    item = localizar(pendencia)
    collection.delete_one(item)