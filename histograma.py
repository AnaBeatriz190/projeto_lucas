import pandas as pd
import matplotlib.pyplot as plt

# Substitua 'seu_arquivo.csv' pelo caminho para o seu arquivo CSV
# O arquivo deve ter pelo menos uma coluna numérica para o histograma
arquivo_csv = 'histograma.csv'

# Ler o arquivo CSV usando pandas
df = pd.read_csv(arquivo_csv)

# Exibir as primeiras linhas do DataFrame para entender a estrutura dos dados
print(df.head())

# Supondo que a coluna para o histograma se chame 'coluna_numerica'
coluna_para_histograma = 'coluna_numerica'

# Plotar o histograma
plt.figure(figsize=(10, 6))
plt.hist(df[coluna_para_histograma], bins=20, edgecolor='black')
plt.title('Histograma de ' + coluna_para_histograma)
plt.xlabel(coluna_para_histograma)
plt.ylabel('Frequência')
plt.grid(True)
plt.show()
