print(f'''
                      Quem pode doar sangue?


 A doação de sangue dura em média 30 minutos e para ser feita
 alguns requisitos devem ser respeitados, como:


 *   Ter entre 18 e 69 anos. Mas menores de 18, podem ser


    doadores a partir dos 16 anos, se tiverem a autorização dos
   seus responsáveis e atenderem aos demais requisitos;


 *   Pesar no mínimo 50 Kg;


 *   Os homens só podem doar sangue uma vez a cada 3 meses e no
   máximo 4 vezes por ano;
   
 *   As mulheres a cada 4 meses e no máximo 3 vezes por ano;


 


  Para ver os detalhes sobre esses e outros requisitos, acesse:


   Fundação Pró-Sangue - Requisitos básicos para doação.''')
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
e = input("""Você gostaria de ser um doador de sangue?
Ss ou Nn?\n""")
listapacientes = []
tps = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
if e.lower() == 's':
    ndp = 1
    while True:
        print("Exelente!Vamos iniciar seu cadastro:")
        n = input("Digite seu nome:")
        s = input("Sexo:")
        i = int(input("Idade:"))
        p = float(input("Peso:"))
        t = int(input("Telefone:"))
        b = input("Em que bairro você mora?")
        c = input("E ele fica em que cidade?")
        print(f"""Tipo de sangue existentes:
                    {tps}""")
        ts = input("qual o seu?")
        if ts not in tps:
            while True:
                print("tipo invalido")
                ts = input("qual o seu?")
                if ts in tps:
                    print("tipo valido")
                    break
        if i >= 18 and p >= 50:
            dessavez = {}
            dessavez.update({"nome": n, "sexo": s,"idade":i,"peso":p, "telefone":t,"bairro":b,"cidade":c,"tps":s})
            listapacientes.append(dessavez)
            print(f'''
            Prontinho, agora você é um dos nossos doadores.
            Saiba que com apenas 1 doação o seu sangue é
            capaz de salvar até 4 pessoas. Então é por elas
            e por outras milhões de vidas que nós agradecemos
            imensamente. Muito obrigado, por ser um doador(a).''')
        else:
            print("você não atende aos requisitos")    
        e2 = input("""Deseja realizar um novo cadastro?
        Ss ou Nn?\n""")
        if e2.lower() == "s":
            pass
        elif e2.lower() == "n":
            print("="*25)
            contador = 0
            for elemento in listapacientes:
              if isinstance(elemento, dict):
                contador += 1
                for bao in range(contador):
                  print(f"""nome:{listapacientes[bao]["nome"]}
sexo:{listapacientes[bao]["sexo"]}
idade:{listapacientes[bao]["idade"]}
peso:{listapacientes[bao]["peso"]}
Telefone:{listapacientes[bao]["telefone"]}
Bairro:{listapacientes[bao]["bairro"]}
Cidade:{listapacientes[bao]["cidade"]}
""")
                  if contador > 1:
                     print("="*25)
            break
        else:
            print("="*25)
            print("vou entender isso como um nao")
            contador = 0
            for elemento in listapacientes:
              if isinstance(elemento, dict):
                contador += 1
                for bao in range(contador):
                  print(f"""nome:{listapacientes[bao]["nome"]}
sexo:{listapacientes[bao]["sexo"]}
idade:{listapacientes[bao]["idade"]}
peso:{listapacientes[bao]["peso"]}
Telefone:{listapacientes[bao]["telefone"]}
Bairro:{listapacientes[bao]["bairro"]}
Cidade:{listapacientes[bao]["cidade"]}
""")
                  if contador > 1:
                     print("="*25)
            break
elif e.lower() == "n":
    print("sem alma")
else:
    print("""vou entender isso como um nao..."
    SEM ALMA!""")