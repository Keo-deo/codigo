x = '5'

try:

  r = x*5

except:
  print("Ta errado aluno")

else:  
  print(f'{r} é o resultado da operação: {x}-2')

finally:
  print("independente do final..:\nbom trabalho")