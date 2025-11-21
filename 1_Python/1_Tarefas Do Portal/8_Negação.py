a = input("escreva a mensagem secreta:\n")
b = a.count("~")
c = -1
d = 0
while a.count("~"):
  c = a.find("~", c + 1)
  d = a.find("¬", d + 1)
  g = a[c+1:d]
  a = a[d+1:]
  print(f"a mensagem secreta é: {g}")