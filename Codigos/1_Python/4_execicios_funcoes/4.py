def par_ou_impar(n):
    if n % 2 == 0:
        return f"O numero {n} é par."
    else:
        return f"O numero {n} é impar."
n = int(input("digite um numero:"))
print(par_ou_impar(n))