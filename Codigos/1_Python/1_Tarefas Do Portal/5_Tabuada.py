a = input(" 1) = todas\n 2) = especifica. \n Escolha se quer uma tabuada especifica ou de todas elas:")
#todas
if a == "1":
  print("Só vai até a do dez!")
  print("----------------------------------------------------------------------------------")
  for b in range(1,11):
    ci = ("-"*10)
    print(ci)
    for c in range(1,11):
      print(f"{b} x {c} = {b*c}")
#especifica
elif a == "2":
  print("\n Só vai até a do dez!")
  d = int(input(" qual delas?:"))
  print("----------------------------------------------------------------------------------")
  for c in range(1,11):
    print(f"{d} x {c} = {d*c}")