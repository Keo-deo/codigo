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

def busca_por_email_tmp(email) -> dict:
    res = {}
    for pessoa in pessoas:
        if pessoa["email"] == email:
            res = pessoa
            break
    return res
while True:
    print("""
opções:
      1-cadastrar pessoa
      2-listar pessoas
      3-pesquisar pessoas
      4-atualizar dados da pessoa
      5-deletar pessoa
      0-sair""")
    escolha = int(input("escolha uma das opções:\n"))
    if escolha == 1:
        nome_da_pessoa_a_cadastrar = input("digite o nome da pessoa que voce quer cadastrar:")
        email_da_pessoa_a_cadastrar = input("digite o email da pessoa que voce quer cadastrar:")
        data_de_nascimento_da_pessoa_a_cadastrar = input("digite a data de nascimento da pessoa que voce quer cadastrar:")
        dados_da_pessoa_a_cadastrar = {"nome" : nome_da_pessoa_a_cadastrar,
                                       "email": email_da_pessoa_a_cadastrar,
                                       "data_de_nascimento":data_de_nascimento_da_pessoa_a_cadastrar}
        pessoas.append(dados_da_pessoa_a_cadastrar)

    if escolha == 2:
        print('Pessoas:')
        for pessoa in pessoas:
            print(f"    - {pessoa['nome']}")
    if escolha == 3:
        email_a_pesquisar = input("digite o email que voce quer pesquisar:")
        result = busca_por_email_tmp(email_a_pesquisar)
        print(f"{result}")

    if escolha == 0:
        break