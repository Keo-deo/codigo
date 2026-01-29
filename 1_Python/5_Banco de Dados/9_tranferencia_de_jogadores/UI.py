from BEI import ad_jogador, exibir_all, jog_expecifico, atualizar_preco, del_jog
import time


print("""Este programa foi criado com o intuito de consultar
o preco de transferencia de jogadores""")

while True:
    print("""\n Opções:
  → 1-Adicionar jogador
  ↗ ↑ ↖
    2-Exibir todos os jogadores cadastrados
    3-Exibir um jogador expecifico
    4-Atualizar preco de tranferencia de um jogador
    5-Excluir um jogador do cadastro
    0-Encerrar do programa
    \n""")

    escolha = int(input("""Para escolher uma das opcoes usando os numeros
    EX: caso queira escolher "adicionar jogador" digite 1.
    Escolha uma das opções:"""))

    if escolha == 1:
        nome = input("Escolha o nome do jogador a cadastrar: ")
        preco = input(f"""O preco deve ser em real( R$ ).
Digite o preco de transferencia do {nome}:""")
        ad_jogador(nome,preco)

    elif escolha == 2:
        exibir_all()

    elif escolha == 3:
        nome = input("Digite o nome do jogador que voce quer achar:")
        jog_expecifico(nome)

    elif escolha == 4:
        nome = input("Digite o nome do jogador que voce quer atualizar o preco:")
        novo_preco = input(f"Digite o novo preco de transferencia do {nome}:")
        atualizar_preco(nome, novo_preco)

    elif escolha == 5:
        nome = input("Digite o nome do jogador que voce quer excluir do cadastro:")
        del_jog(nome)

    elif escolha == 0:
        print("Encerrando programa...")
        time.sleep(2)
        break

    else:
        print("Esta opção nao existe")