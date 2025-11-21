from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["arvore"]

colection = db["conhecidos"]

seletor = {"trabalho": "Instrutor de Programação"}

print(colection.find_one( seletor ))

novo = { 
    "$set": {
        'nome' : "Victor Matheus Barbosa Tavares"
    }
}
colection.update_one(seletor, novo)

print(colection.find_one( seletor ))
