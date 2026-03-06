def gato_manhoso():
    sly_cat = f'''
     |\\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
    |,4-  ) )-,_. ,\\ (  `'-'
   '---''(_/--'  `-'\\_)
'''
    print(sly_cat)          
def gato_fedido():
    smelly_cat = f'''
_._     _,-'""`-._
(,-.`._,'(       |\\`-/|
   `-.-' \\ )-`( , o o)
         `-    \\`_`"'-
'''
    print(smelly_cat)
def pouca_comida():
    little_food = f'''
              __
             / _)
    _.----._/ /
   /         /
__/ (  | (  |
/__.-'|_|--|_|
'''
    print(little_food)

print("""esse programa demonstra algums dos desenhos do julio
    
      digite o numero do desenho que deseja ver:
      1 - gato manhoso
      2 - gato fedido
      3 - pouca comida""")
desenho = int(input("\nDigite o numero do desenho: "))
if desenho == 1:
    gato_manhoso()
elif desenho == 2:
    gato_fedido()
elif desenho == 3:
    pouca_comida()
else:
    print("Esse desenho não está disponivel")