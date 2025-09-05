print("""este programa calcula seu IMC(indice de massa muscular)
--_--_-_--_---____---__-_-_------_--__--____--_--__--__----___----_--_-_--_---____---__-_-_------_--__--____--_--__--__----___--
      """)
while True:
  p = float(input("digite seu peso:"))
  a = float(input("digite sua altura:"))
  imc = float(p/a**2)
  if imc < 18.5:
    ca = "Abaixo do peso"
  elif imc >= 18.5 and imc <= 24.9:
    ca = "Normal"
  elif imc >= 25.0 and imc <= 29.9:
    ca = "Sobrepeso"
  elif imc >= 30.0 and imc <= 39.9:
    ca = "Obesidade Tipo 1"
  elif imc >= 40.0:
    ca = "Obesidade Tipo 2"
  print(f"seu IMC é:{imc:.1f} e sua classificação é:{ca}")
  a = input("Quer calcular o IMC de mais alguem?\n")
  if a == "NAO" or a == "NÃO" or a == "nao" or a == "não" or a == "Não" or a == "Nao":
    break