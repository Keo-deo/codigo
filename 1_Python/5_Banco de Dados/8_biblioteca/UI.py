from autor import *
from genero_livro import passs
from genero import *
from livro import passs

while True:
    escolha = str(input("""opcoes:
          a1-adicionar autor
          a2-
          a3-
          a4-
          a5-
          a6-
          0-
"""))
    
    if escolha.lower() == "a1":
        add_autor()

    if escolha.lower() == "a2":
        ex_autor()

    if escolha.lower() == "a3":
        psq_autor()

    if escolha.lower() == "a4":
        pass

    if escolha.lower() == "a5":
        pass

    if escolha.lower() == "0":
        pass