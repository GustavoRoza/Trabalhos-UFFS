import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV
data = pd.read_csv('./Results/resultados.csv')

# Criação do gráfico
plt.figure(figsize=(10, 6))

# Plota os valores da coluna '% do ótimo' por algoritmo
for algoritmo in data['algoritmo'].unique():
    subset = data[data['algoritmo'] == algoritmo]
    plt.plot(subset['instancia'], subset['% do ótimo'], label=algoritmo, marker='o')

# Adiciona título e rótulos
plt.title('Performance dos Algoritmos Comparados ao Ótimo')
plt.xlabel('Instância')
plt.ylabel('% do ótimo')

# Adiciona legenda
plt.legend(loc='best')

# Salva o gráfico como PDF
plt.savefig('grafico_resultados.pdf')

# Mostra o gráfico na tela (opcional)
plt.show()
