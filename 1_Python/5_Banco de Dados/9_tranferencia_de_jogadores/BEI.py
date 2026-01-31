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

#def jog_especifico(nome):
    #jog = colection.find_one({"nome": nome})
    #print(f"""Se aparecer "none" é porque o jogador nao esta cadastrado
#Nome:{jog["nome"]} | Preço: R$ {jog["preco"]}""")
    #return jog

def jog_especifico(nome):
    jog = colection.find_one({"nome": nome})
    return jog

def atualizar_preco(nome, novo_preco):
    n_preco = {
        "preco": novo_preco
    }
    colection.update_one({"nome": nome}, {"$set": n_preco})

def del_jog(nome):
    try:
        item = jog_especifico(nome)
        colection.delete_one(item)
    except:
        return "none"