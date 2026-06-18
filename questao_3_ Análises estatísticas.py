print("--- 1. PREPARANDO E LIMPANDO OS DADOS DE FILMES ---")
# Filtrando apenas as linhas que são Filmes (Movie)
filmes = df[df['type'] == 'Movie'].copy()

# Removendo o texto ' min' e transformando a duração em números inteiros para podermos fazer contas
filmes['duration_num'] = filmes['duration'].str.replace(' min', '').astype(float)

print("Dados limpos com sucesso! Calculando as medidas centrais...\n")

print("--- 2. MEDIDAS DE TENDÊNCIA CENTRAL ---")
# Calculando a Média, Mediana e Moda estatística
media_duracao = filmes['duration_num'].mean()
mediana_duracao = filmes['duration_num'].median()
moda_duracao = filmes['duration_num'].mode()[0]

print(f"- Média de duração: {media_duracao:.2f} minutos")
print(f"- Mediana de duração: {mediana_duracao:.1f} minutos")
print(f"- Moda de duração (tempo que mais se repete): {moda_duracao:.0f} minutos\n")

print("--- 3. EXTREMOS (MAIS CURTO E MAIS LONGO) ---")
# Encontrando o menor e o maior tempo
id_mais_curto = filmes['duration_num'].idxmin()
id_mais_longo = filmes['duration_num'].idxmax()

print(f"- Filme mais curto: '{filmes.loc[id_mais_curto, 'title']}' com {filmes.loc[id_mais_curto, 'duration_num']:.0f} min.")
print(f"- Filme mais longo: '{filmes.loc[id_mais_longo, 'title']}' com {filmes.loc[id_mais_longo, 'duration_num']:.0f} min.")
