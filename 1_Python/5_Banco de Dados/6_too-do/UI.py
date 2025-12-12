from BEI import adicionar, exibir, localizar, alterar, deletar

print("""Bem-vindo ao sistema de gerenciamento de Pendencias.
      você pode adicionar , exibir , localizar , alterar e deletar uma pendencia.
      \n""")
      
      
while True:
    print("""opções:
      1 - adicionar pendencia
      2 - exibir pendencias
      3 - localizar pendencia
      4 - alterar status da pendencia
      5 - deletar uma pendencia
      0 - sair
      """)
    
    escolha = int(input("escolha uma das opções acima:"))

    if escolha == 1:
        pendencia = input("Digite o nome da pendencia que deseja adicionar:\n")
        adicionar(pendencia)
    
    elif escolha == 2:
        exibir()
    
    elif escolha == 3:
        pendencia = input("Digite o nome da pendencia que deseja localizar:\n")
        localizar(pendencia)

    elif escolha == 4:
        pendencia = input("Digite o nome da pendencia que deseja alterar:\n")
        alterar(pendencia)
        print("pendencia alterada com sucesso.")

    elif escolha == 5:
        pendencia = input("Digite o nome da pendencia que deseja deletar:\n")
        deletar(pendencia)
        print("pendencia deletada com sucesso.")

    elif escolha == 0:
        print("encerrando o programa.")
        break

    else:
        print("opção inválida, encerrando o programa.")
        break