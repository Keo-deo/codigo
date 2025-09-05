tupla = (3,5,2,9,1,4,6,8,7,0)
lista = []
while True:
  a = input("Digite um numero:")
  for b in range(len(tupla)):
    if a in tupla[b]:
      lista.insert(tupla.index(a),a)
      print(f"adicionado"+
            f"{lista}")
    elif a not in tupla:
      pass