from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["arvore"]

colection = db["conhecidos"]

seletor = {"nome": "Victor mateus"}

colection.delete_one( seletor )
