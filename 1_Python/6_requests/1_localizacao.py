import requests

# Este site devolve o seu IP e sua localização aproximada
url = "http://ip-api.com/json/"

try:
    print("Buscando sua localização aproximada...")
    res = requests.get(url)
    dados = res.json()
    
    cidade = dados.get('city', 'Desconhecida')
    estado = dados.get('regionName', 'Desconhecido')
    
    print(f"Parece que você está em: {cidade} - {estado}!")
except:
    print("Não consegui conectar à internet.")