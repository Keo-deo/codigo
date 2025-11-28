from funcoes import pessoas,cadastrar,listar,pesquisar,atualizar,deletar

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

    if escolha == 2:
        peoples = listar()
        print(f"""{peoples}
""")

    if escolha == 3:
        email_a_pesquisar = input("digite o email que voce quer pesquisar:")
        result = pesquisar(email_a_pesquisar)
        print(f"{result}")

    if escolha == 4:
        email = input('escolha o email da pessoa a atualizar:')
        nome = input('Digite o novo nome: ')
        n_email = input('Digite o novo e-mail: ')
        birthdate = input('Digite a nova data de nascimento: ')

        pessoa = {}
        if nome != '':
            pessoa = atualizar(email, 'nome', nome)
        if birthdate != '':
            pessoa = atualizar(email,"data_de_nascimento",birthdate)
        if n_email != '':
            pessoa = atualizar(email,"email",n_email)
        

    if escolha == 5:
        deletar()        

    if escolha == 0:
        break