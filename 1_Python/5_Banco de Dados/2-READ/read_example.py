from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["arvore"]

colection = db["conhecidos"]


#LISTAR TODOS
for doc in colection.find():
    print(doc)
print("_-_"*50)
#BUSCAR por dicionario que tenha tal valor dentro
print(colection.find_one({"trabalho": "Instrutor de Programação"}))
