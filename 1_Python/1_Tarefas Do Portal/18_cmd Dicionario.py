livro = {"a":"b","c":"d","e":"f","g":"h"}
print(livro["a"],"e",livro["c"])
livro["i"] = "j"
print(f"""{livro}
      {livro["i"]}""")
livro.update([("k", "l"), ('m', 'n')])
print(f"""{livro}
      {livro["k"]}
      {livro["m"]}""")
livro.update([("a","z")])
print(livro["a"])
livro["a"] = "b"
print(livro["a"])
print(livro.keys())
print(livro.values())
print(livro.items())
tambor = livro.items()
if "h" in tambor:
    print("tá")
w = livro.pop(18,"num existe")
print(f"""{livro}
      {w}""")
y = livro.get(5,"num existe tambem")
print(f"""{livro}
      {y}""")
#len funciona com dicionario{}
#clear funciona com dicionario{}
#pop funciona com dicionario{}
#in funciona com dicionarios{}
#
#