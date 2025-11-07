def tabuada(n):
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
num = int(input("Digite um numero para ver a tabuada: "))
tabuada(num)