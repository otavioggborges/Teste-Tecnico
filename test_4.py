# Definindo o faturamento mensal por estado
faturamentoMensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o faturamento total
faturamentoTotal = sum(faturamentoMensal.values())

# Calculando o percentual de representação de cada estado
percentuais = {estado: (valor / faturamentoTotal) * 100 for estado, valor in faturamentoMensal.items()}

# Exibindo os resultados
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")