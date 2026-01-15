def verificar_idade(ano):
    idade = 2026 - ano
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
ano_nascimento = int(input("Digite seu ano de nascimento: "))
print(f"Voce é {verificar_idade(ano_nascimento)}.")