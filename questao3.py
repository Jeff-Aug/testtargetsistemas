import json

# Abrir e ler o arquivo JSON
with open('questao3.json', 'r') as file:
    dados = json.load(file)

# Filtra apenas os dias com faturamento maior que zero
valores = [d["valor"] for d in dados if d["valor"] > 0]

# Calcula o menor e maior valor de faturamento
menor_valor = min(valores)
maior_valor = max(valores)

# Calcula a média mensal (ignora dias sem faturamento)
media_mensal = sum(valores) / len(valores)

# Conta os dias com faturamento acima da média mensal
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

# Exibe os resultados
print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")