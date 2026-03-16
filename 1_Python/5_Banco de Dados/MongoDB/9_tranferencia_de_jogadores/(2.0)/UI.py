from BEI import ad_jogador, exibir_all, jog_expecifico, atualizar_preco, del_jog
import questionary
import time


print("""Este programa foi criado com o intuito de consultar
o preco de transferencia de jogadores""")

while True:
    escolha = questionary.select(
        "\nOpções:",
        choices=[
            "Adicionar jogador",
            "Exibir todos os jogadores cadastrados",
            "Exibir um jogador expecifico",
            "Atualizar preço de tranferencia de um jogador",
            "Excluir um jogador do cadastro",
            "Encerrar do programa"
        ]
    ).ask()

    if escolha == "Adicionar jogador":
        nome = input("Escolha o nome do jogador a cadastrar: ")
        preco = input(f"""O preço deve ser em real( R$ ).
Digite o preco de transferencia do {nome}:""")
        ad_jogador(nome,preco)

    elif escolha == "Exibir todos os jogadores cadastrados":
        exibir_all()

    elif escolha == "Exibir um jogador expecifico":
        nome = input("Digite o nome do jogador que voce quer achar:")
        jog_expecifico(nome)

    elif escolha == "Atualizar preço de tranferencia de um jogador":
        nome = input("Digite o nome do jogador que voce quer atualizar o preço:")
        novo_preco = input(f"Digite o novo preco de transferencia do {nome}:")
        atualizar_preco(nome, novo_preco)

    elif escolha == "Excluir um jogador do cadastro":
        nome = input("Digite o nome do jogador que voce quer excluir do cadastro:")
        del_jog(nome)

    elif escolha == "Encerrar do programa":
        print("Encerrando programa...")
        time.sleep(2)
        break