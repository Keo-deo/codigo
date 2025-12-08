from funcoes import cadastrar,listar,pesquisar,atualizar,deletar

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
        nome = input('escolha o nome da pessoa a cadastrar:')
        email = input('escolha o email da pessoa a cadastrar:')
        data_nascimento = input('escolha data de nascimento da pessoa a cadastrar:')
        cadastrar(nome,email,data_nascimento)

    elif escolha == 2:
        peoples = listar()
        print(f"""{peoples}
""")

    elif escolha == 3:
        email_a_pesquisar = input("digite o email que voce quer pesquisar:")
        result = pesquisar(email_a_pesquisar)
        print("aqui está o resultado da pesquisa:")
        print(f"{result}")

    elif escolha == 4:
        email = input('escolha o email da pessoa a atualizar:')
        n_nome = input('Digite o novo nome: ')
        n_email = input('Digite o novo e-mail: ')
        n_birthdate = input('Digite a nova data de nascimento: ')
        atualizar(email, n_nome, n_email, n_birthdate)
    elif escolha == 5:
        email = input('escolha o email da pessoa a deletar:')
        deletar(email)

    elif escolha == 0:
        print("encerrando o programa.")
        break
    
    else:
        print("opção inválida, encerrando o programa.")
        break