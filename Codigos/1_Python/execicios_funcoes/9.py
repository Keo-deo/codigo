def area_triangulo(base, altura):
    return (base * altura) / 2
b = float(input("Digite a base do triangulo: "))
a = float(input("Digite a altura do triangulo: "))
print(f"A area do triangulo é {area_triangulo(b, a)}")