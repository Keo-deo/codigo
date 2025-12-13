d = int(input("digite a quantidade de dias que voce ficou com o carro:"))

km = float(input("digite a quantidade de km rodados:"))

preco_d = d * 60
preco_km = km * 0.15
preco_t = preco_d + preco_km

print("\n",f"o total a pagar é{preco_t}")