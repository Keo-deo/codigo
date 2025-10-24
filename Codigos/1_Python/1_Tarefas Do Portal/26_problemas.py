

def testar_divisao():
    try:
        n1 = int(input("Digite um numero"))
        n2 = int(input("Digite um numero"))
        resultado = n1/n2
        return resultado
    except ZeroDivisionError:
        print("Erro de divisao por zero")
    except ValueError:
        print("Voce digitou uma letra")

def testar_valor():
    try:
        n1 = int(input("Digite um numero"))
        n1 = int(input("Digite um numero"))

