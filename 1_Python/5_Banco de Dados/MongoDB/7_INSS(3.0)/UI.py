from BEI import texto_informacoes,verificar_usuario, ad_user_c_d, ad_user_s_d

print("""Bem vindo! Voce esta usando o mais novo sitema do INSS, o INSS 3.0!""")

while True:
    pmv =  input("Voce já possui cadastro no sistema? (s/n):")
    if pmv.lower() == "n":
        print("Iniciando seu cadastro!")
        usuario = input("Digite seu nome de usuario:")
        senha = input("Digite sua senha:")
        quer_dica = input("Você deseja adicionar uma dica para caso se esqueça sua senha? (s/n):")
        if quer_dica.lower() == "s":
            dica = input("Digite sua dica:")
            ad_user_c_d(usuario, senha, dica)
            
        elif quer_dica.lower() == "n":
            ad_user_s_d(usuario, senha)
    elif pmv.lower() == "s":
        e_m_pmv_s = input("""escolha uma das opcoes abaixo:
1 - Verificar informacoes
2 - calcular quanto tempo falta para a aposentadoria
Digite o numero da opcao desejada:""")
        if e_m_pmv_s == "1":
            print(texto_informacoes) 

        elif e_m_pmv_s == "2":
            pass

