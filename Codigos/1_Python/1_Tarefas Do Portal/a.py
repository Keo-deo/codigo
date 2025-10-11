def somar(n1, n2):
    global resultado
    resultado = n1 + n2
n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
somar(n1, n2)
print("O resultado da soma é:", resultado)

def mensagem(msg:str, emoticon = ' '):
 '''
 Essa função exibe uma mensagem para o usuário. Se desejar,
 ela também pode exibir um emoticon.
 '''

 print(f'\n{msg}')

  #Então por padrão a mensagem sempre será exibida sem um emoticon,

  #Mas se o usuário inserir um valor diferente do padrão.
 if emoticon != ' ':
   print(f'\n{emoticon}') #Esse emoticon vai aparecer na tela.

mensagem('Olá Mundo')
mensagem('Tudo bem?', '😄')