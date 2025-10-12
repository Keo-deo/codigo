alfabeto_latino = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
alfabeto_russo = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я")
def verificar_latino(l1,l2):
    if l1 in alfabeto_latino and l2 in alfabeto_latino:
        l1_index = alfabeto_latino.index(l1)
        l2_index = alfabeto_latino.index(l2)
        if l1_index < l2_index:
            letras_latino = alfabeto_latino[l1_index:l2_index+1]
            print(f"letras entre {l1} e {l2} são: {letras_latino}")
        else:
            letras_latino = alfabeto_latino[l2_index:l1_index+1]                                        #O russo nao pegou
            print(f"letras entre {l1} e {l2} são: {letras_latino}")
def verificar_russo(l1,l2):
    if l1 in alfabeto_russo and l2 in alfabeto_russo:
        l1_index = alfabeto_russo.index(l1)
        l2_index = alfabeto_russo.index(l2)
        if l1_index < l2_index:
            letras_russo = alfabeto_russo[l1_index:l2_index+1]
            print(f"letras entre {l1} e {l2} são: {letras_russo}")
        else:
            letras_russo = alfabeto_russo[l2_index:l1_index+1]
            print(f"letras entre {l1} e {l2} são: {letras_russo}")
print("""Este programa mostra todas as letrs entre duas letras que você escolher.
      E não so isso, você pode escolher entre o alfabeto latino e o alfabeto russo.""")
alfabeto_escolhido = int(input("""Escolha o alfabetos:
      1 - Alfabeto latino
      2 - Alfabeto russo
      Digite o numero do alfabeto que deseja usar: """))
l1 = input("Digite a primeira letra: ").lower()
l2 = input("Digite a segunda letra: ").lower()
if alfabeto_escolhido == 1:
    if l1 in alfabeto_latino and l2 in alfabeto_latino:
        if l1 == l2:
            print(f"As letras entre {l1} e {l2} são: {l1}")
        elif l1 != l2:
            verificar_latino(l1,l2)
    else:
        print("""uma ou ambas as letras não pertencem ao alfabeto latino.
        encerrando o programa.""")        
elif alfabeto_escolhido == 2:
    if l1 in alfabeto_russo and l2 in alfabeto_russo:
        if l1 == l2:
            print(f"As letras entre {l1} e {l2} são: {l1}")
        elif l1 != l2:
            verificar_russo(l1,l2)
    else:
        print("""uma ou ambas as letras não pertencem ao alfabeto russo.
        encerrando o programa.""")