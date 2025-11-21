from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["arvore"]

colection = db["conhecidos"]

seletor = {"trabalho": "Instrutor de Programação"}

colection.delete_one( seletor )
