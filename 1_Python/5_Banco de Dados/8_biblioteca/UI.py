from autor import *
from genero_livro import passs
from genero import *
from livro import passs

while True:
    escolha = str(input("""opcoes:
        a1-adicionar autor
        a2-exibir todos os autores
        a3-pesquisar um autor expecifico
        a4-atualizar as informacoes de um autor
        a5-excluir um autor
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        b1-adicionar genero
        b2-exibir todos os generos
        b3-pesquisar um genero expecifico
        b4-atualizar as informacoes de um genero
        b5-excluir um genero
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        c1-adicionar livro
        c2-exibir todos os livros
        c3-pesquisar um livro expecifico
        c4-atualizar as informacoes de um livro
        c5-excluir um livro
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        d1-
        d2-
        d3-
        d4-
        d5-
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        0-encerrar programa
"""))

#          AUTOR    
    if escolha.lower() == "a1":
        nome = str(input("Digite o nome do autor: "))
        birthdate = str(input("Digite a data de nascimento do autor (DD/MM/AAAA): "))
        add_autor(nome, birthdate)

    elif escolha.lower() == "a2":
        print(ex_autor())

    elif escolha.lower() == "a3":
        nome = str(input("Digite o nome do autor que deseja pesquisar: "))
        print(psq_autor(nome))

    elif escolha.lower() == "a4":
        nome = str(input("Digite o nome do autor que deseja atualizar: "))
        n_nome = str(input("Digite o novo nome do autor: "))
        n_birthdate = str(input("Digite a nova data de nascimento do autor (DD/MM/AAAA): "))
        upd_autor(nome, n_nome, n_birthdate)

    elif escolha.lower() == "a5":
        nome = str(input("Digite o nome do autor que deseja excluir: "))
        del_autor(nome)

#          GENERO
    elif escolha.lower() == "a1":
        add_autor()

    elif escolha.lower() == "a2":
        ex_autor()

    elif escolha.lower() == "a3":
        psq_autor()

    elif escolha.lower() == "a4":
        pass

    elif escolha.lower() == "a5":
        pass

#          LIVRO
    elif escolha.lower() == "0":
        pass

    elif escolha.lower() == "a1":
        add_autor()

    elif escolha.lower() == "a2":
        ex_autor()

    elif escolha.lower() == "a3":
        psq_autor()

    elif escolha.lower() == "a4":
        pass

    elif escolha.lower() == "a5":
        pass

    elif escolha.lower() == "0":
        break

    else:
        print("opcao invalida, tente novamente")