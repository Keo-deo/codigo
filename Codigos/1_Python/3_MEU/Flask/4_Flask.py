from flask import Flask

app = Flask(__name__)


@app.route("/")
pmv = True
if pmv == True:
  print("Olá bem vindo(a) ao nosso mais novo programa de INSS\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  pao = input("Indentificamos que essa é sua primeira vez aqui.\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\niniciando cadastro\nPor Favor digite seu nome:\n")
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  oap = input("Por segurança defina uma senha de acesso:\n")
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
  pou = input('Voce gostaria de criar uma dica para caso esqueca sua senha?')
  if pou == 'sim' or pou == 'SIM' or pou == 'Sim':
    iep = input('insira sua dica:\n')
  elif pou == 'não' or pou == 'NÃO' or pou == 'Não' or pou == 'nao' or pou == 'Nao' or pou == 'NAO':
    print('certo')
  else:
    print("Vou entender isso como um não")
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nCadastro realizado com sucesso.")
  pmv = False
  an = input("Entrando em modo espera\nclique enter para dasativar\n")
if pmv == False:
  oda = input("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\na) entrar  b) sair\n")
  niep = 3
  print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nParece que voce ja esteve aqui antes")
  if oda == "a" or oda == "A":
    while niep != 0:
      print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_")
      tup = input("Digite o seu nome\n")
      tap = input("\nDigite sua senha\n")
      if tup != pao:
        print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nSeu impostor!\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nPrograma encerredo")
        break
      if tap != oap:
        if pou == 'sim' or pou == 'SIM' or pou == 'Sim':
          if(niep >= 2):
            print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nSenha incorreta sua dica é\n",iep)
            niep -= 1
            print("\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nlhe resta",niep,"tentativas\n")
          else:
            niep -= 1
            print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nSenha incorreta\n-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nlhe resta",niep,"tentativa\n")
            if niep == 0:
             print("Nº de tentivas excedidas\nPrograma encerrado")
             break
      if tup == pao and tap == oap:
        print("-__-___--_-___-__----_-_-__-__-_-_-_--__--_---_--_-_-------_-__-_---_\nAcesso liberado. Bem vindo",pao)
        print("Como já dito antes este programa serve para calcular quanto tempo falta para alguem se aposentar...\nConciderando que o tempo de aposentadoria padrão (65 anos)")
        print("----------------------------------------------------------------------------------")
        idade = int(input("Qual a sua idade?"))
        v = int(idade - 65)
        print("----------------------------------------------------------------------------------")
        print("Faltam", v ,"anos para a aposentadoria")
        a = 2025 - idade + 65
        print("E isso sera no ano de",a)
        break
  elif oda == "b" or oda == "B":
    print("Programa encerrado")
  else:
      print("Escolha invalida\nEncerrando programa")
if __name__ == "__main__":
    app.run()