import time
lc = []
lnc = []
while True:
  m = input("a): Cadastrar um novo cliente | b) Remover um cliente cadastrado | c): Exibir lista de clientes cadastrados | d): Sair do programa\n")
  if m == "a" or m == "A":
    c = input("Digite o nome do cliente: ")
    nc = input("digite o numero do cliente:")
    if len(nc) >= 8 and len(nc) <= 9:
      lc.append(c)
      lnc.append(nc)
    else:
      print("numero invalido")
  if m == "b" or m == "B":
    cr = input("digite o nome do cliente que quer remover:")
    lnc.pop(lc.index(cr))
    lc.remove(cr)
  if m == "c" or m == "C":
    for i in range(len(lc)):# nao consegui deixar em ordem alfabetica
      print(f"o",i+1,"° cliente é:",lc[i],"e o seu numero é:",lnc[i])
  if m == "d" or m == "D":
    print("Fechando programa")
    break