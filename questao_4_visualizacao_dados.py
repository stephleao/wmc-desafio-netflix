import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Link alternativo e atualizado que usamos no Colab
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv'
df = pd.read_csv(url)

# --- TRATAMENTO DOS DADOS PARA OS GRÁFICOS ---
todos_generos = df['listed_in'].str.split(', ').explode()
filmes = df[df['type'] == 'Movie'].copy()
filmes['duration_num'] = filmes['duration'].str.replace(' min', '').astype(float)
media_duracao = filmes['duration_num'].mean()
mediana_duracao = filmes['duration_num'].median()

# Configurando o estilo visual dos gráficos
sns.set_theme(style="whitegrid")

print("--- GRÁFICO 1: TOP 10 GÊNEROS MAIS FREQUENTES ---")
plt.figure(figsize=(12, 6))
top_generos = todos_generos.value_counts().head(10)
sns.barplot(x=top_generos.values, y=top_generos.index, palette="viridis")
plt.title("Top 10 Gêneros Mais Frequentes no Catálogo da Netflix", fontsize=14, fontweight='bold')
plt.xlabel("Quantidade de Títulos", fontsize=12)
plt.ylabel("Gênero", fontsize=12)
plt.tight_layout()
plt.show()

print("\n--- GRÁFICO 2: HISTOGRAMA DA DURAÇÃO DOS FILMES ---")
plt.figure(figsize=(10, 6))
sns.histplot(data=filmes, x='duration_num', bins=30, kde=True, color="royalblue")
plt.axvline(media_duracao, color='red', linestyle='--', linewidth=2, label=f'Média: {media_duracao:.1f} min')
plt.axvline(mediana_duracao, color='green', linestyle='-', linewidth=2, label=f'Mediana: {mediana_duracao:.1f} min')
plt.title("Distribuição da Duração dos Filmes (Netflix)", fontsize=14, fontweight='bold')
plt.xlabel("Duração (em minutos)", fontsize=12)
plt.ylabel("Frequência (Quantidade de Filmes)", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()
