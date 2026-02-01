from BEI import ad_jogador, exibir_all, jog_expecifico, atualizar_preco, del_jog
import time

print("                 Bem vindo!")
print("Este é o Sistema de Transferência de Jogadores")

print("""Escolha uma das opções abaixo:
        1-Adicionar jogador
        2-Exibir todos os jogadores
        3-Exibir jogador específico
        4-Atualizar preço de transferencia de um jogador
        5-Deletar jogador
        0-Sair
""")

while True:
    escolha = int(input("""Para escolhe uma opção,
digite o número correspondente: """))
    

    if escolha == 1:
        nome = input("Nome do jogador que voce deseja cadastrar: ")
        preco = input("Preço do jogador que voce deseja cadastrar (em R$): ")
        ad_jogador(nome, preco)
        print(f"{nome} adicionado com sucesso!")

    elif escolha == 2:
        print("Lista de Jogadores cadastrado:\n")
        exibir_all()
    
    elif escolha == 3:
        nome = input("Digite o nome do jogador que deseja achar: ")
        jog_expecifico(nome)

    elif escolha == 4:
        nome = input("Digite o nome do jogador que deseja atualizar o preço: ")
        novo_preco = input("Digite o novo preço de transferência (em R$): ")
        atualizar_preco(nome, novo_preco)
        print(f"Preço de transferencia, de {nome} atualizado com sucesso!")

    elif escolha == 5:
        nome = input("Digite o nome do jogador que deseja deletar: ")
        resultado = del_jog(nome)

    elif escolha == 0:
        print("Encerrando sistema...")
        time.sleep(2)
        break

    else:
        print("Esta opção não existe.")