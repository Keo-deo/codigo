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
<<<<<<< HEAD:1_Python/5_Banco de Dados/9_tranferencia_de_jogadores/BEI.py
        print(f'nome: {jog['nome']} | valor de transferência: {jog['preco']}')
=======
        print(f"Nome:{jog["nome"]} | Preço: R$ {jog["preco"]}")
>>>>>>> 47e63ffc7286d4a92896ba56db25b21dd56e5df6:1_Python/5_Banco de Dados/9_tranferencia_de_jogadores/(2.0)/BEI.py

def jog_expecifico(nome):
    jog = colection.find_one({"nome": nome})
    print(f"""Se aparecer "none" é porque o jogador nao esta cadastrado
<<<<<<< HEAD:1_Python/5_Banco de Dados/9_tranferencia_de_jogadores/BEI.py
{jog["nome"]} | {jog["preco"]}""")
=======
Nome:{jog["nome"]} | Preço: R$ {jog["preco"]}""")
>>>>>>> 47e63ffc7286d4a92896ba56db25b21dd56e5df6:1_Python/5_Banco de Dados/9_tranferencia_de_jogadores/(2.0)/BEI.py
    return jog

def atualizar_preco(nome, novo_preco):
    n_preco = {
        "preco": novo_preco
    }
    colection.update_one({"nome": nome}, {"$set": n_preco})

def del_jog(nome):
    try:
        item = jog_expecifico(nome)
        colection.delete_one(item)
    except:
        print("none")