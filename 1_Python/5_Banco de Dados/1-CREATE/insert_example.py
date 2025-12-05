from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["arvore"]

colection = db["conhecidos"]

# dados_one = { "nome": "alyne", 'idade': 33, 'trabalho': 'Peixe Vivo' }
# res = colection.insert_one( dados )
dados_many = [
    { "nome":"vitor", 'idade': 27, 'trabalho': 'programador' },
    { "nome":"Victor matheus", 'idade': 31, 'trabalho': 'Instrutor de Programação' }
]
res=colection.insert_many(dados_many)
print(res)
