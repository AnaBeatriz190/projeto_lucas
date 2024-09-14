import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo CSV
arquivo_csv = 'histograma.csv'

# Ler o arquivo CSV usando pandas
df = pd.read_csv(arquivo_csv)

# Exibir as primeiras linhas do DataFrame para entender a estrutura dos dados
print(df.head())

# A coluna que contém as alturas dos alunos é 'Altura dos Alunos'
coluna_para_histograma = 'Altura dos Alunos'

# Plotar o histograma
plt.figure(figsize=(10, 6))
plt.hist(df[coluna_para_histograma], bins=10, edgecolor='black')  # Ajustei o número de bins para 10
plt.title('Histograma das Alturas dos Alunos')
plt.xlabel('Altura dos Alunos')
plt.ylabel('Frequência')
plt.grid(True)

# Exibir a imagem do histograma
plt.savefig("gráfico_em_histograma.png")
