import json
dados = '''
[
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 2000.0},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 3000.0},
    {"dia": 5, "valor": 4000.0}
]
'''

faturamento = json.loads(dados)

def calcular_faturamento(dados):
    valores = [d["valor"] for d in dados if d["valor"] > 0]
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_da_media = len([v for v in valores if v > media])
    return menor, maior, dias_acima_da_media

menor, maior, dias_acima_media = calcular_faturamento(faturamento)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média: {dias_acima_media}")
