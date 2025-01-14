import json

def analisar_faturamento():
    with open("faturamento.json") as arquivo:
        dados = json.load(arquivo)
    
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]  # Ignora valores zero
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_da_media = sum(1 for valor in valores if valor > media)
    
    return menor, maior, dias_acima_da_media

# Teste
menor, maior, dias = analisar_faturamento()
print(f"Menor valor: {menor}, Maior valor: {maior}, Dias acima da média: {dias}")