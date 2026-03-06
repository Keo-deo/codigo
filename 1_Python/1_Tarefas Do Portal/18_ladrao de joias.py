suspeitos = [

#Nome:            Sexo: Cabelo:  Altura:  Peso:        Hooby:
('Anita Bath',      'F', 'Ruivo',  'Alto',     'Magro', 'Jogos de Azar'), #0
('Anne Arthy',      'F', 'Loiro', 'Baixo',    'Normal',    'Jardinagem'), #1
('Barb Dwyer',      'M', 'Loiro', 'Medio', 'Sobrepeso',      'Esportes'), #2
('Catherine Stark', 'F', 'Preto', 'Medio',     'Magro',         'Artes'), #3
('Constantino B.',  'F', 'Preto',  'Alto',     'Magro',    'Literatura'), #4
('Olena Mendes',    'F', 'Calvo', 'Baixo',    'Normal',          'Moda'), #5
('Peter P.',        'M', 'Preto', 'Medio',    'Normal',    'Fotografia'), #6
('Sr.Bozzo',        'M', 'Calvo',  'Alto', 'Sobrepeso',    'Tecnologia'), #7
('Tenorio Salazar', 'M', 'Ruivo', 'Baixo',     'Obeso',       'Caçador'), #8
('W. Lionheart',    'F', 'Loiro', 'Medio',    'Normal',       'Felinos'), #9 


]

pistas = (
 '\n1º Pista: \n O suspeito foi visto entrando em um carro, rumo ao aeroporto\n',
 
 '\n2º Pista: \n Na cena do crime, uma testemunha afirmou que o ladrão tinha mãos femininas\n',

 '\n3º Pista: \n Antes de embarcar, o suspeito fugiu pelos dutos de ar do aeroporto.\n',

 '\n4º Pista: \n A bagagem deixada para trás era uma bomba, \n'+
 'mas encontramos um fio loiro em seus destroços.\n',
   
 '\n5º Pista: \n A amostra de DNA não pode ser concluída, \n'+
 'mas uma de suas botas continha um passe para o Parque Nacional Kruger.\n',

 '\n6º Pista: \n Aos arredores do Parque, um turista foi visto em posse de uma jóia.\n'+
 'Ele tinha uma altura mediana e estava conversando com Traficantes de Marfim.\n',

 '\nFim de Jogo: \n O suspeito foi capturado em uma emboscada, \n'+
 'pegamos ela com a esmeralda, em uma das trilhas do Safári.\n'
)

fala_jornal = """“Um colar de esmeraldas, que pertenceu à princesa Isabel, foi furtado do Museu Nacional Quinta da Boa Vista, localizado no Rio de Janeiro e recentemente recuperado de um incêndio. O furto ocorreu durante um evento internacional que, por meio da exposição das jóias da família real, tentava angariar fundos para a ampliação e restauração do acervo do museu. Por enquanto a polícia segue investigando o caso, mas os suspeitos não tiveram seus nomes divulgados."""

print(fala_jornal+
      suspeitos+
      pistas
      )

homens  = set(); mulheres  = set()
calvos  = set(); loiros    = set(); pretos  = set(); ruivos = set()
altos   = set(); medios    = set(); baixos  = set()
obesos = set(); sobrepesos = set(); normais = set(); magros = set()
for s in suspeitos:

 if s == suspeitos[0]:
   s_f  = ''; s_m  = ''; 
 if s[1] in 'F':
   mulheres.update(s)
   s_f += '| '+s[0]

 else:
   homens.update(s)
   s_m += '| '+s[0]
print(pistas[0])
print('\nTodos os elementos ainda são suspeitos...')
print(pistas[1])
print('\nHomens descartados da lista de suspeitos, exibindo os dados das mulheres:\n')
print(mulheres)
print(pistas[2])
print('\nExibindo os dados das mulheres que caberiam em um duto de ventilação:\n')
print((mulheres & (normais | magros)))
print(pistas[3])
print('\nExibindo os dados das mulheres loiras que se encaixam nesse perfil:\n')
mulheres_loiras = mulheres & loiros
print('\n', (mulheres_loiras & (normais | magros )))
print(pistas[4])
print('\nNo momento, as duas mulheres ainda são suspeitas...')
print(pistas[5])
acusado = mulheres_loiras & ((normais | magros) & medios)
print('\nDados do Acusado: \n', acusado)
for i in suspeitos:
 if i[0] in acusado:
   print('\nEnviado um mandato de prisão para ', i[0])