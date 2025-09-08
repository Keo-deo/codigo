
tps = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
tb_SangueInfo = (
 {'tipo':'A+',
   'doa':('A+', 'AB+'),
   'recebe':('A+', 'A-', 'O-', 'O+')},
 {'tipo':'A-',
   'doa':('A+', 'A-', 'AB+', 'AB-'),
   'recebe':('A-', 'O-')},
 {'tipo':'B+',
   'doa':('B+', 'AB+'),
   'recebe':('B+', 'B-', 'O-', 'O+')},
 {'tipo':'B-',
   'doa':('B+', 'B-', 'AB+', 'AB-'),
   'recebe':('B-', 'O-')},
 {'tipo':'AB+',
   'doa':'AB+',
   'recebe':tps},
 {'tipo':'AB-',
   'doa':('AB+', 'AB-'),
   'recebe':('A-','B-','AB-', 'O-')},
 {'tipo':'O+',
   'doa':('A+', 'B+', 'AB+', 'O+'),
   'recebe':('O+', 'O-')},
 {'tipo':'O-',
   'doa':tps,
   'recebe':'O-'},)
while True:
    print('Tipos de Sangue Existentes: \n', tps)
    sangue = input('\nQual é o seu? \n').upper()
    if sangue in tps:
        print('\nInformações sobre o seu tipo sanguíneo:')
        sangueID = tps.index(sangue)
        sangueIF = tb_SangueInfo[sangueID]
        print(f'''
        Tipo: {sangueIF["tipo"]}\n
        Pode doar para:
        {sangueIF["doa"]}\n
        E pode receber doações de:
        {sangueIF["recebe"]}\n''')
        break
    else:
        print('\nPor favor, digite um tipo válido.\n')
input('Digite qualquer tecla para continuar \n')
