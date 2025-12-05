pessoas = [
    {
        'nome' : 'Victor',
        'email': 'victor@gmail.com',
        'data_de_nascimento': '2025-11-21'
    },
    {
        'nome' : 'matheus',
        'email': 'matheus@gmail.com',
        'data_de_nascimento': '2025-11-21'
    },
    {
        'nome' : 'murilo',
        'email': 'murilo@gmail.com',
        'data_de_nascimento': '2025-11-21'
    }
]

def cadastrar(nome, email, birthdate):
    pessoa = {
        'nome' : nome,
        'email': email,
        'data_de_nascimento': birthdate
    }
    pessoas.append(pessoa)

#---------------------------------------------------------------------------------------------------------
def listar():
    return pessoas

#---------------------------------------------------------------------------------------------------------
def pesquisar(email) -> dict:
    pessoa = {}
    for p in pessoas:
        if p["email"] == email:
            pessoa = p
            break
    return pessoa

#---------------------------------------------------------------------------------------------------------
def atualizar(email, campo, valor):
    pessoa = pesquisar(email)
    if campo in pessoa.keys():
        pessoa[campo] = valor
        return pessoa
    return { }

def atualizar(email, campo1, valor1, campo2, valor2):
    a = atualizar(email,campo1,valor1)
    b = atualizar(email,campo2,valor2)
    att = a | b
    return att

def atualizar(email, campo1, valor1, campo2, valor2, campo3, valor3):
    a = atualizar(email,campo1,valor1) 
    b = atualizar(email,campo2,valor2)
    c = atualizar(email,campo3,valor3)
    att = a | b | c
    return att

#---------------------------------------------------------------------------------------------------------
def deletar(email):
    pessoa = pesquisar(email)
    pessoas.remove(pessoa)