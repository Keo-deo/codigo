import getpass

print("blablabla bem vindo")
print("pedra(1):1° quebra a tesoura /2° esmaga lagarto")
print("papel(2):1° embrulha a pedra /2° refulta o spock")
print("tesoura(3):1° corta papel /2° mata lagarto")
print("lagarto(4):1° envenena Spock /2° come papel")
print("spock(5):1° destroi tesoura /2° vaporiza pedra")
jog1 = input("jogador 1:")
opc1 = int(getpass.getpass("escolha?:"))
jog2 = input("jogador 2:")
opc2 = int(getpass.getpass("escolha?:"))
if opc1 == 1 and opc2 == 1:
  print("empate")
elif opc1 == 1 and opc2 == 2:
  print(jog2,"venceu")
elif opc1 == 1 and opc2 == 3:
  print(jog1,"venceu")
elif opc1 == 1 and opc2 == 4:
  print(jog1,"venceu")
elif opc1 == 1 and opc2 == 5:
  print(jog2,"venceu")
elif opc1 == 2 and opc2 == 1:
  print(jog2,"venceu")
elif opc1 == 2 and opc2 == 2:
  print("empate")
elif opc1 == 2 and opc2 == 3:
  print(jog2,"venceu")
elif opc1 == 2 and opc2 == 4:
  print(jog2,"venceu")
elif opc1 == 2 and opc2 == 5:
  print(jog1,"venceu")
elif opc1 == 3 and opc2 == 1:
  print(jog1,"venceu")
elif opc1 == 3 and opc2 == 2:
  print(jog1,"venceu")
elif opc1 == 3 and opc2 == 3:
  print("empate")
elif opc1 == 3 and opc2 == 4:
  print(jog1,"venceu")
elif opc1 == 3 and opc2 == 5:
  print(jog2,"venceu")
elif opc1 == 4 and opc2 == 1:
  print(jog2,"venceu")
elif opc1 == 4 and opc2 == 2:
  print(jog1,"venceu")
elif opc1 == 4 and opc2 == 3:
  print(jog2,"venceu")
elif opc1 == 4 and opc2 == 4:
  print("empate")
elif opc1 == 4 and opc2 == 5:
  print(jog1,"venceu")
elif opc1 == 5 and opc2 == 1:
  print(jog1,"venceu")
elif opc1 == 5 and opc2 == 2:
  print(jog2,"venceu")
elif opc1 == 5 and opc2 == 3:
  print(jog1,"venceu")
elif opc1 == 5 and opc2 == 4:
  print(jog2,"venceu")
elif opc1 == 5 and opc2 == 5:
  print("empate")
else:
  print("erro")