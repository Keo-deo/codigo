from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["arvore"]

colection = db["conhecidos"]

# pessoas = [
#     {
#         'nome' : 'Victor',
#         'email': 'victor@gmail.com',
#         'data_de_nascimento': '2025-11-21'
#     },
#     {
#         'nome' : 'matheus',
#         'email': 'matheus@gmail.com',
#         'data_de_nascimento': '2025-11-21'
#     },
#     {
#         'nome' : 'murilo',
#         'email': 'murilo@gmail.com',
#         'data_de_nascimento': '2025-11-21'
#     }
# ]

def cadastrar(nome, email,data_de_nascimento):
    dados_pessoa = {
        'nome' : nome,
        'email': email,
        'data_de_nascimento': data_de_nascimento
    }
    res = colection.insert_one(dados_pessoa)
    print(res)

def listar():
    #LISTAR TODOS
    for doc in colection.find():
        print(doc)
    print("_-_"*50)
    #BUSCAR por dicionario que tenha tal valor dentro
    print(colection.find_one({"trabalho": "Instrutor de Programação"}))