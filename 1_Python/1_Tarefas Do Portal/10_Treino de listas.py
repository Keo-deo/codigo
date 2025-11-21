listaDeObjetos = ['Copo','Colher','Prato']
print(f'Lista de Objetos: {listaDeObjetos}\n')
for i in range(len(listaDeObjetos)):
 print(f'{i} Elemento da Lista: {listaDeObjetos[i]}')
print(len(listaDeObjetos))
print('O índice do Copo é: ', listaDeObjetos.index("Copo"))
print('O índice da colher é: ', listaDeObjetos.index("Colher"))
print('O índice do Prato é: ', listaDeObjetos.index("Prato"))
a = ['A','B','C']
b = ['D','E','F']
ab = a+b
print(f'''
A  = {a}
B  = {b}
AB = {ab}''')
lista = []
print("\n\nLista Vazia: ", lista)
lista[0:] = 'A'
#Obs. Se na lista, esse índice já estiver ocupado, não é necessário o uso dos ‘:’
print("1º Elemento da Lista: ", lista)
lista[0:4] = 'B','C','D','E'
#Note que o 'A' devido a sua posição, foi trocado pelo B.
print("Demais elementos da Lista: ", lista)
#      adicionar
docesFavoritos = []
print('Digite o nome dos seus 3 doces favoritos: \n')
for i in range(1,4):
 docesFavoritos.append(str(input(f'\n{i}º Doce: \n')))
print('\nLista de Doces: \n', docesFavoritos)
docesFavoritos.extend(['Trufa de Chocolate Amargo', 'Brigadeiro de Limão'])
print('\nLista de Doces Expandida: \n',docesFavoritos)
docesFavoritos.insert(3,'Bolinho')
print('\nLista de Doces c/ Bolinho: \n',docesFavoritos)
for i in range(1,4):
 if 'Torta de Maracujá' in docesFavoritos:
    docesFavoritos.remove('Torta de Maracujá')
    print(f"{i}º Lista de Doces, sem torta:\n{docesFavoritos}\n")
 elif 'Brigadeiro de Café' in docesFavoritos:
    docesFavoritos.pop(1) #Sem parâmetro, o pop remove o último item da lista.
    print(f'{i}º Lista de Doces, sem cafeína:\n{docesFavoritos}\n')
 else:
    docesFavoritos.clear()
    print(f'{i}º Na verdade, você não merece nenhum doce.\n{docesFavoritos}\n')