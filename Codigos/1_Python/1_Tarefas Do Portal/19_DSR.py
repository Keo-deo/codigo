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

e = input("""Você gostaria de ser um doador de sangue?
Ss ou Nn?\n""")
w = {}
tps = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
if e == 'S' or e == "s":
    for z in range(999):
        print("Exelente!Vamos iniciar seu cadastro:")
        n = input("Digite seu nome:")
        s = input("Sexo:")
        i = input("Idade:")
        p = input("Peso:")
        t = input("Telefone:")
        b = input("Em que bairro você mora?")
        c = input("E ele fica em que cidade?")
        print(f"""Tipo de sangue existentes:
                  {tps}""")
        s = input("Qual o seu?:")
        w.update([("np1",n),("sp1",s),("ip1",i),("pp1",p),("tp1",t),("bp1",b),("cp1",c),("sp1",s)])
        print(f'''
        Prontinho, agora você é um dos nossos doadores.
        Saiba que com apenas 1 doação o seu sangue é
        capaz de salvar até 4 pessoas. Então é por elas
        e por outras milhões de vidas que nós agradecemos
        imensamente. Muito obrigado, por ser um doador(a).''')
        e2 = input("""Deseja realizar um novo cadastro?
        Ss ou Nn?\n""")
        if e2 == "S" or e2 == "s":
            pass
        elif e2 == "N" or e2 == "n":
            break
        else:
            print("Vou entender isso como um Nn")
            break
