from BEI import *

print("""Este programa foi criado com o intuito de consultar
o preco de transferencia de jogadores""")

while True:
    print("""\n Opções:
    1-adicionar jogador
    2-exibir todos os jogadores cadastrados
    3-exibir um jogador expecifico
    4-atualizar preco de tranferencia de um jogador
  → 5-excluir um jogador do cadastro
  ↗ ↑ ↖
    \n""")

    escolha = int(input("""Para escolher uma das opcoes usando os numeros
    EX: caso queira escolher "adicionar jogador" digite 1
    escolha uma das opções:"""))

    if escolha == 1:
        nome = input("escolha o nome do jogador a cadastrar: ")
        preco = input(f"digite o preco de transferencia do {nome} em milhões:")
        ad_jogador(nome,preco)

    elif escolha == 2:
        pass

    elif escolha == 3:
        pass

    elif escolha == 4:
        pass

    elif escolha == 5:
        pass

    elif escolha == 0:
        print("Encerrando programa...")
        break

    else:
        print("esta nao existe")