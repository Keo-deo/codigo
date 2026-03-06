print("1 elefante incomoda muita gente")
numero_de_elefantes = 10
for i in range(2, numero_de_elefantes + 1):
    incomodam = "incomodam " * i + "muito mais"
    if i % 2 == 0:
        print(f"{i} elefantes {incomodam}")
    else:
        print(f"{i} elefantes incomodam muita gente")