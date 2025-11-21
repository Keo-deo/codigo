l1 = ["Angela Merkel","Guilherme Briggs","Moon Jae-in","Papa Francisco","Neil Gaiman","Malala Yousafzai","Felipe Neto","Jean Bauch","Jacinda Arden","Tim Cook"]
l2 = ["Barack Obama","Malala Yousafzai","Marcos Silva","Neil Gaiman","Robson Kumode","Jacinda Arden","Tim Minchin","André Lima","Justin Trudeau","Tongo"]
l3 = ["Papa Francisco","Clóvis de Barros Filho","Sanna Marin","Mônica Ruediger","Tim Minchin","Cellbit","Tongo","Marcos Silva","Lenin Moreno","Michile Giudice"]
l4 = []
for i in range(10):
  for x in range(10):
    if l1[i] == l2[x] or l1[i] == l3[x]:
      l4.append(l1[i])
print(l4,'verificando o "l1"')
for i in range(10):
  for x in range(10):
    if l2[i] == l1[x] or l2[i] == l3[x]:
      l4.append(l2[i])
print(l4,'verificando o "l2"')
for i in range(10):
  for x in range(10):
    if l3[i] == l1[x] or l3[i] == l2[x]:
      l4.append(l3[i])
print(l4,'verificando o "l3"')
l5 = []
for i in range(len(l4)):
  if l4[i] not in l5:
    l5.append(l4[i])
print(sorted(l5))