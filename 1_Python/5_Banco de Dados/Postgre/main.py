import psycopg2

try:
    #configurando conexacao
    conn = psycopg2.connect(
        dbname="meu_primeiro_banco",# Nome do banco que você criou
        user="postgres",             # Usuario padrao
        password="145344",          # A senha que você definiu na instalacao
        host="localhost",           # Endereco do seu computador
        port="5432"                 # A porta padrao
    )

    # Criar um cursor para executar comandos
    cur = conn.cursor()
    
    # Executar uma consulta simples
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print(f"Conectado ao: {db_version}")

    # Fechar conexoes
    cur.close()
    conn.close()

except Exception as e:
    print(f"erro ao conectar {e}")