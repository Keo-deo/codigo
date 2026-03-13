import random

palavras = [
    ["maca", "banana", "melancia", "manga", "abacaxi", "pera", "pera"],#fruta
    ["jbl", "samsung", "apple", "microsoft", "logitech", "lg", "aoc"],#marca de eletronicos
    ["tom holland", "michael jackson", "the rock", "elon musk", "neymar", "bill gates", "messi"],#famoso
    ["eua", "brasil", "mexico", "espanha", "franca", "inglaterra", "japao"],#pais
    ["cachorro", "gato", "jacare", "elefante", "porco", "vaca", "coruja"],#animal
]

genero_aleatorio = random.choice(list(palavras))

if "maca" in genero_aleatorio:
    genero_escolhido = "fruta"

elif "jbl" in genero_aleatorio:
    genero_escolhido = "marca de eletronicos"

elif "neymar" in genero_aleatorio:
    genero_escolhido = "famoso"

elif "eua" in genero_aleatorio:
    genero_escolhido = "pais"

elif "gato" in genero_aleatorio:
    genero_escolhido = "animal"

palavra_escolhida = random.choice(genero_aleatorio)

# Cria uma lista de traços para cada letra da palavra
tracos = ["-"] * len(palavra_escolhida)

print(f"Gênero: {genero_escolhido}")
print("Palavra secreta:", " ".join(tracos))  # Mostra os traços separados por espaço

boneco = {
    "7 tentativas": """
  /----|
 |     |
 |
 |
 |
 |________""",

    "6 tentativas": """
  /----|
 |     |
 |     O
 |
 |
 |________""",

    "5 tentativas": """
  /----|
 |     |
 |     O
 |     |
 |
 |________""",

    "4 tentativas": """
  /----|
 |     |
 |     O
 |    /|
 |
 |________""",
    
    "3 tentativas": """
  /----|
 |     |
 |     O
 |    /|\\
 |
 |________""",

    "2 tentativas": """
  /----|
 |     |
 |     O
 |    /|\\
 |    / 
 |________""",

    "1 tentativas": """
  /---|
 |    |
 |    O
 |   /|\\
 |   / \\
 |________"""
}

tentativas = 7

letras_tentadas = []

while tentativas > 0 and "-" in tracos:
    # Mostra o boneco baseado nas tentativas restantes
    chave_boneco = f"{tentativas} tentativas"
    if chave_boneco in boneco:
        print(boneco[chave_boneco])
    
    print("Palavra:", " ".join(tracos))
    print("Letras tentadas:", ", ".join(letras_tentadas))
    
    letra = input("Digite uma letra: ").lower().strip()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra válida!")
        continue
    
    if letra in letras_tentadas:
        print("Você já tentou essa letra!")
        continue
    
    letras_tentadas.append(letra)
    
    if letra in palavra_escolhida.lower():
        # Substitui os traços pelas letras corretas nas posições certas
        for i, char in enumerate(palavra_escolhida.lower()):
            if char == letra:
                tracos[i] = palavra_escolhida[i]  # Mantém a capitalização original
        print("Acertou!")
    else:
        tentativas -= 1
        print("Errou! Tentativas restantes:", tentativas)

if "-" not in tracos:
    print("Parabéns! Você ganhou!")
    print("Palavra:", " ".join(tracos))
else:
    print(boneco["1 tentativas"])
    print("Você perdeu! A palavra era:", palavra_escolhida)