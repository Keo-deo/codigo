from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["INSS"]

users_collection = db["users"]

def verificar_usuario(usuario):
    try:
        user = users_collection.find_one({"usuario": usuario})
        return user
    except Exception as e:
        return False
    
def ad_user_c_d(usuario, senha, dica):
    dados = {
        "usuario": usuario,
        "senha": senha,
        "dica": dica
    }
    res = users_collection.insert_one(dados)
    print("Usuario cadastrado com sucesso!")
def ad_user_s_d(usuario, senha):
    dados = {
        "usuario": usuario,
        "senha": senha,
        "dica": "sem dica cadastrada"
    }
    res = users_collection.insert_one(dados)
    print("Usuario cadastrado com sucesso!")

texto_informacoes = """
Existem tres tipos de aposentadoria:
    1 - Aposentadoria por idade
    2 - Aposentadoria por tempo de contribuição
    3 - Aposentadoria especial
                  
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

Tanto a aposentadoria por idade quanto a aposentadoria por tempo de contribuição
possuem os mesmos beneficios, porem os requisitos sao diferentes.
                  
1 - Aposentadoria por idade:
    Requisitos:
        - Homens:   65 anos de idade
                    20 de contribuição
        - Mulheres: 62 anos de idade
                    15 anos de contribuição

2 - Aposentadoria por tempo de contribuição:
    Requisitos:
        - Homens:   64 anos de idade
                    35 anos de contribuição
        - Mulheres: 59 anos de idade
                    30 anos de contribuição
Benefícios de ambos:
        - Direito a aposentadoria integral
        - Acesso a benefícios adicionais
        - Piso (valor minimo) R$ 1.518,00 por mês
        - Teto (valor maximo) R$ 8.157,00 por mês
                  
A aposentadoria especial é destinada a trabalhadores que exercem atividades
consideradas prejudiciais à saúde ou à integridade física
    Requisitos:
        Baixo risco: 25 anos de contribuição
                     60 anos de idade
        Médio risco: 20 anos de contribuição
                     55 anos de idade
        Alto risco:  15 anos de contribuição
                     55 anos de idade
    Benefícios:
        - Direito a aposentadoria integral
        - Acesso a benefícios adicionais
        - Piso (valor minimo) R$ 1.518,00 por mês
        - Teto (valor maximo) R$ 8.157,00 por mês"""