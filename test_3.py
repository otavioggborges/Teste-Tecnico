import json

# Função para carregar dados do arquivo dados.json
def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Função para realizar os cálculos
def calculate_statistics(data):
    # Extrair os valores de faturamento, ignorando os dias sem faturamento
    faturamentos = [dia['valor'] for dia in data if dia['valor'] > 0]

    # Calcula o menor valor
    menor_faturamento = min(faturamentos)
    
    # Calcula o maior valor
    maior_faturamento = max(faturamentos)

    # Calcula a média
    media_faturamento = sum(faturamentos) / len(faturamentos)

    # Contar o número de dias superior à média
    dias_acima_da_media = len([faturamento for faturamento in faturamentos if faturamento > media_faturamento])

    # Retornar os resultados
    return menor_faturamento, maior_faturamento, dias_acima_da_media

filepath = 'dados.json'
dados = load_data(filepath)
menor_faturamento, maior_faturamento, dias_acima_da_media = calculate_statistics(dados)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")