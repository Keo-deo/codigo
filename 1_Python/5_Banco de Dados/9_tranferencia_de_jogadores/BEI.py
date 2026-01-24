from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["tranferencia_de_jogadores"]

colection = db["jogadores"]

def ad_jogador(nome, preco):
    dados_jogador = {
        "nome": nome,
        "preco": preco
    }

    res = colection.insert_one(dados_jogador)

def exibir_all():
    for jog in colection.find():
        print(jog)

def jog_expecifico(nome):
    jog = colection.find_one({"nome": nome})
    print(f"""Se aparecer "none" é porque o jogador nao estra cadastrado
          {jog}""")
    return jog