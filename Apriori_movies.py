import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

dados = pd.read_excel(r'C:\Users\Felipe\Desktop\ml-latest-small\ratings.xlsx')

dados = dados[dados['Apriori'] == 1]

matriz_apriori = (dados
                  .groupby(['userId', 'nome_filme'])['Apriori']
                  .max()
                  .unstack()
                  .fillna(0)
                  .astype(bool))

#Executar o Algoritmo Apriori
# min_support = 0.05 significa que o filme/combinação deve aparecer em pelo menos 5% dos usuários
itens_frequentes = apriori(matriz_apriori, min_support=0.05, use_colnames=True)

#Gerar as Regras de Associação normalmente
regras = association_rules(itens_frequentes, metric="confidence", min_threshold=0.5)

#FILTRO: Limitar a quantidade de filmes no antecedente (Ex: no máximo 2 filmes)
regras = regras[regras['antecedents'].apply(lambda x: len(x)) <= 2]

#Configurar o Pandas para não cortar o texto na tela
pd.set_option('display.max_colwidth', None)

#Limpar o visual removendo a palavra "frozenset"
regras['antecedents'] = regras['antecedents'].apply(lambda x: ', '.join(list(x)))
regras['consequents'] = regras['consequents'].apply(lambda x: ', '.join(list(x)))

#Ordenar as regras filtradas pelas mais fortes
regras = regras.sort_values(by=['lift', 'confidence'], ascending=False)

regras.to_excel('resultado_regras_apriori_2.xlsx', index=False)

#print(regras[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(30))
