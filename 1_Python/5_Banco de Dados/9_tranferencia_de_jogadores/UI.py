from BEI import ad_jogador, jog_especifico, atualizar_preco, del_jog
from pymongo import MongoClient
import tkinter as tk

db = MongoClient("mongodb://localhost:27017/")

client = db["tranferencia_de_jogadores"]

colection = client["jogadores com tk"]

janela = tk.Tk()
janela.title("Sistema de Transferência de Jogadores")
janela.geometry("500x500")

janela_inicial = tk.Frame(janela)
janela_inicial.pack()

tk.Label(janela_inicial, text="Este é o Sistema de Transferência de Jogadores").pack()
tk.Label(janela_inicial, text="Escolha uma das opções abaixo:").pack()

def pg_ad_jogador():
    janela_ad_jogador = tk.Frame(janela)
    janela_inicial.pack_forget()
    janela_ad_jogador.pack()
    tk.Label(janela_ad_jogador, text="Para adicionar um jogador, preencha os campos abaixo:\n").pack()
    tk.Label(janela_ad_jogador, text="Nome do jogador:").pack()
    nome_entry = tk.Entry(janela_ad_jogador)
    nome_entry.pack()
    tk.Label(janela_ad_jogador, text="Preço do jogador:").pack()
    preco_entry = tk.Entry(janela_ad_jogador)
    preco_entry.pack()
    def voltar():
        janela_ad_jogador.pack_forget()
        janela_inicial.pack()
    def confirmar():
        nome = nome_entry.get()
        preco = preco_entry.get()
        ad_jogador(nome, preco)
        tk.Label(janela_ad_jogador, text=f"{nome} adicionado com sucesso!").pack()
        janela_ad_jogador.pack_forget()
        janela_inicial.pack()
    tk.Label(janela_ad_jogador, text="").pack()
    tk.Button(janela_ad_jogador, text="Confirmar", command=confirmar).pack()
    tk.Label(janela_ad_jogador, text="").pack()
    tk.Button(janela_ad_jogador, text="Voltar", command=voltar).pack()


tk.Label(janela_inicial, text="").pack()   
tk.Button(janela_inicial, text="Adicionar Jogador", command=pg_ad_jogador).pack()


def pg_exibir_all():
    janela_exibir_all = tk.Frame(janela)
    janela_inicial.pack_forget()
    janela_exibir_all.pack()
    tk.Label(janela_exibir_all, text="Lista de Jogadores cada:\n").pack()
    for jog in colection.find():
        tk.Label(janela_exibir_all, text=f"Nome: {jog['nome']} | Preço: R$ {jog['preco']}").pack()
    def voltar():
        janela_exibir_all.pack_forget()
        janela_inicial.pack()
    tk.Label(janela_exibir_all, text="").pack()
    tk.Button(janela_exibir_all, text="Voltar", command=voltar).pack()

tk.Label(janela_inicial, text="").pack()
tk.Button(janela_inicial, text="Exibir Todos os Jogadores", command=pg_exibir_all).pack()


def pg_jog_especifico():
    janela_jog_expecifico = tk.Frame(janela)
    janela_inicial.pack_forget()
    janela_jog_expecifico.pack()
    tk.Label(janela_jog_expecifico, text="Para consultar  um jogador específico,").pack()
    tk.Label(janela_jog_expecifico, text="preencha os campos abaixo: \n").pack()
    tk.Label(janela_jog_expecifico, text="Nome do jogador:").pack()
    nome_entry = tk.Entry(janela_jog_expecifico)
    nome_entry.pack()
    def voltar():
        janela_jog_expecifico.pack_forget()
        janela_inicial.pack()
    def confirmar():
        nome = nome_entry.get()
        jog = jog_especifico(nome)
        tk.Label(janela_jog_expecifico, text=f"Nome: {jog['nome']} | Preço: R$ {jog['preco']}").pack()
        
    tk.Label(janela_jog_expecifico, text="").pack()
    tk.Button(janela_jog_expecifico, text="Confirmar", command=confirmar).pack()
    tk.Label(janela_jog_expecifico, text="").pack()
    tk.Button(janela_jog_expecifico, text="Voltar", command=voltar).pack()
    tk.Label(janela_jog_expecifico, text="").pack()

tk.Label(janela_inicial, text="").pack()
tk.Button(janela_inicial, text="Consultar um jogador específico", command=pg_jog_especifico).pack()


def pg_atualizar_preco():
    janela_atualizar_preco = tk.Frame(janela)
    janela_inicial.pack_forget()
    janela_atualizar_preco.pack()
    tk.Label(janela_atualizar_preco, text="Para atualizar o preço de um jogador,").pack()
    tk.Label(janela_atualizar_preco, text="preencha os campos abaixo: \n").pack()
    tk.Label(janela_atualizar_preco, text="Nome do jogador:").pack()
    nome_entry = tk.Entry(janela_atualizar_preco)
    nome_entry.pack()
    tk.Label(janela_atualizar_preco, text="Novo preço do jogador:").pack()
    preco_entry = tk.Entry(janela_atualizar_preco)
    preco_entry.pack()
    def voltar():
        janela_atualizar_preco.pack_forget()
        janela_inicial.pack()
    def confirmar():
        nome = nome_entry.get()
        n_preco = preco_entry.get()
        atualizar_preco(nome, n_preco)
    tk.Label(janela_atualizar_preco, text="").pack()
    tk.Button(janela_atualizar_preco, text="Confirmar", command=confirmar).pack()
    tk.Label(janela_atualizar_preco, text="").pack()
    tk.Button(janela_atualizar_preco, text="Voltar", command=voltar).pack()

tk.Label(janela_inicial, text="").pack()
tk.Button(janela_inicial, text="Atualizar Preço de um Jogador", command=pg_atualizar_preco).pack()


def pg_del_jog():
    janela_del_jog = tk.Frame(janela)
    janela_inicial.pack_forget()
    janela_del_jog.pack()
    tk.Label(janela_del_jog, text="Para deletar um jogador do sistema de cadastro,").pack()
    tk.Label(janela_del_jog, text="preencha os campos abaixo: \n").pack()
    tk.Label(janela_del_jog, text="Nome do jogador:").pack()
    nome_entry = tk.Entry(janela_del_jog)
    nome_entry.pack()
    def voltar():
        janela_del_jog.pack_forget()
        janela_inicial.pack()
    def confirmar():
        nome = nome_entry.get()
        tentativa = del_jog(nome)
        if tentativa == "none":
            tk.Label(janela_del_jog, text="Jogador não encontrado no sistema.").pack()
        elif tentativa != "none":
            tk.Label(janela_del_jog, text=f"{nome} deletado com sucesso!").pack()
    tk.Label(janela_del_jog, text="").pack()
    tk.Button(janela_del_jog, text="Confirmar", command=confirmar).pack()
    tk.Label(janela_del_jog, text="").pack()
    tk.Button(janela_del_jog, text="Voltar", command=voltar).pack()

tk.Label(janela_inicial, text="").pack()
tk.Button(janela_inicial, text="Deletar um Jogador", command=pg_del_jog).pack()


def pg_encerrar_programa():
    janela_encerrar_programa = tk.Frame(janela)
    janela_inicial.pack_forget()
    janela_encerrar_programa.pack(expand=True, fill='both')
    tk.Label(janela_encerrar_programa, text="encerrando programa...").pack(pady=220)
    janela.after(2000, janela.quit)

tk.Label(janela_inicial, text="").pack()
tk.Button(janela_inicial, text="Encerrar Programa", command=pg_encerrar_programa).pack()

janela.mainloop()