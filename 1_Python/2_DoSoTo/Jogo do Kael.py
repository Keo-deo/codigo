# prompt: fassa um tente adivinhar o personagem de blue lock

import random

def adivinhar_personagem_blue_lock():
    personagens = {
        "Isagi": "Protagonista, busca ser o melhor artilheiro do mundo.",
        "Bachira": "Gosta de jogar futebol de forma imprevisível e divertida.",
        "Chigiri": "Possui uma velocidade incrível.",
        "Kunigami": "Busca se tornar um super-herói do futebol.",
        "Don lorenzo": "um mendigo que virou jogador de futebol e ama dinheiro."
    }

    personagem_secreto = random.choice(list(personagens.keys()))
    dica = personagens[personagem_secreto]

    print("Bem-vindo ao jogo Adivinhe o Personagem de Blue Lock!")
    print("Você terá algumas tentativas para adivinhar o personagem secreto.")
    print(f"Dica: {dica}")

    tentativas = 3

    while tentativas > 0:
        palpite = input("Qual personagem você acha que é? ").strip()

        if palpite.lower() == personagem_secreto.lower():
            print(f"Parabéns! Você acertou! O personagem era {personagem_secreto}.")
            return
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Errado! Você tem mais {tentativas} tentativa(s).")
            else:
                print(f"Suas tentativas acabaram O personagem era {personagem_secreto}.")

adivinhar_personagem_blue_lock()