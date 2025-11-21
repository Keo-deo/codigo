a = 'aaaaa'; b = 'aaaab'; c = 'aaaba'; d = 'aaabb'
msgCifrada   = 'uniCorniOFlamejanteS'
msgBacon     = ''
msgDecifrada = ''
for i in range(len(msgCifrada)):
 if msgCifrada[i] == msgCifrada[i].lower():
   msgBacon += 'a'
 else:
   msgBacon += 'b'
print('Expectativa: aaabaaaabbaaaabaaaab')
print('Realidade:  ',msgBacon)
print(f'''
Letra 1: {msgBacon[0:5]}
Letra 2: {msgBacon[5:10]}
Letra 3: {msgBacon[10:15]}
Letra 4: {msgBacon[15:20]}''')
for i in range (len(msgBacon)//5):
 start = i*5
 end   = start+5
 letra = msgBacon[start:end]
 if a == letra:
   msgDecifrada += 'a'
 if b == letra:
   msgDecifrada += 'b'
 if c == letra:
   msgDecifrada += 'c'
 if d == letra:
   msgDecifrada += 'd'
print(f'''
msgCifrada:   {msgCifrada}
msgBacon:     {msgBacon}
msgDecifrada: {msgDecifrada}''')