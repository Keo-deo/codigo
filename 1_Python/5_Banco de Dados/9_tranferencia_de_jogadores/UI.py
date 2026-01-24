from BEI import *

print("""Este programa foi criado com o intuito de consultar
o preco de transferencia de jogadores""")

while True:
    print("""\n Opções:
    1-Adicionar jogador
    2-Exibir todos os jogadores cadastrados
    3-Exibir um jogador expecifico
    4-Atualizar preco de tranferencia de um jogador
  → 5-Excluir um jogador do cadastro
  ↗ ↑ ↖
    \n""")

    escolha = int(input("""Para escolher uma das opcoes usando os numeros
    EX: caso queira escolher "adicionar jogador" digite 1.
    Escolha uma das opções:"""))

    if escolha == 1:
        nome = input("Escolha o nome do jogador a cadastrar: ")
        preco = input(f"Digite o preco de transferencia do {nome} em milhões:")
        ad_jogador(nome,preco)

    elif escolha == 2:
        exibir_all

    elif escolha == 3:
        nome = input("Digite o nome do jogador que voce quer achar:")
        jog_expecifico(nome)

    elif escolha == 4:
        pass

    elif escolha == 5:
        pass

    elif escolha == 0:
        print("Encerrando programa...")
        break

    else:
        print("Esta opção nao existe")