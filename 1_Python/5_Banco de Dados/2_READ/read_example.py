from pymongo import MongoClient
from bson.objectid import ObjectId

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["arvore"]

colection = db["conhecidos"]


#LISTAR TODOS
for doc in colection.find():
    print(doc)
print("_-"*75+"_")
#BUSCAR por dicionario que tenha tal valor dentro
# print(colection.find_one({"trabalho": "Instrutor de Programação"}))
print(colection.find_one({"_id": ObjectId("693c6e029d18b84501acd973")}))
