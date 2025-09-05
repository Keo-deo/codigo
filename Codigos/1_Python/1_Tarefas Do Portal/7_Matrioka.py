pmv = True
if pmv == True:
  print("Olá bem vindo(a) ao nosso mais novo programa\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  pao = input("Indentificamos que essa é sua primeira vez aqui\nPorFavor digite seu nome:\n")
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  print("Obrigado",pao)
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  oap = input("mas por segurança,defina uma senha de acesso:\n")
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  iep = input("Perfeito! Agora escreva uma dica para caso esqueça dela.\n")
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nCadastro realizado com sucesso.")
  pmv = False
  an = input("Entrando em modo espera\nclique enter para dasativar\n")
#-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_-
if pmv == False:
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nOpa parece que voce ja esteve aqui antes.")
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  niep = 3
  oda = input("a) entrar  b) sair\n")
  if oda == "a" or oda == "A":
    while niep != 0:
      print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
      tup = input("Digite o seu nome\n")
      tap = input("\nDigite sua senha\n")
      if tup != pao:
        print("Seu impostor!\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nPrograma encerredo")
        break
      if tap != oap:
        if(niep >= 2):
          print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nSenha incorreta sua dica é\n",iep)
          niep -= 1
          print("\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nlhe resta",niep,"tentativas\n")
        else:
          niep -= 1
          print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nSenha incorreta")
          print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nlhe resta",niep,"tentativa\n")
          if niep == 0:
            print("Nº de tentivas excedidas\nPrograma encerrado")
            break
      if tup == pao and tap == oap:
        print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nAcesso liberado. bem vindo",pao)
        break
  elif oda == "b" or oda == "B":
    print("Programa encerrado")
  else:
      print("Escolha invalida")