# Sistema de Recomendação de Filmes com Algoritmo Apriori

Este projeto implementa um sistema de recomendação de filmes utilizando o algoritmo **Apriori** para mineração de regras de associação. O objetivo é analisar o comportamento de usuários (baseado em um subset do dataset MovieLens) para descobrir quais filmes de alta avaliação costumam ser assistidos juntos.

---

## Tecnologias e Bibliotecas Utilizadas
* **Python 3.14+**
* **Pandas**: Para manipulação, limpeza e engenharia de dados (conversão de dados textuais e pivots).
* **Mlxtend (Machine Learning Extensions)**: Para a aplicação do algoritmo Apriori e geração das regras de associação.
* **Openpyxl**: Engine utilizada para leitura e escrita de arquivos integrados ao Microsoft Excel.

---

## Estrutura do Projeto
```text
├── .venv/                   # Ambiente virtual Python (ignorado no git)
├── .gitignore               # Arquivos e extensões ignorados pelo Git
├── Apripori_movies.py       # Script principal de execução do algoritmo
├── requirements.txt         # Dependências do projeto para instalação rápida
└── README.md                # Documentação do projeto
```

---

## Como o Projeto Funciona (Pipeline de Dados)

1. **Carga e Filtro Prévio**: O script carrega as avaliações e filtra a base utilizando a coluna customizada `Apriori == 1`, garantindo que apenas filmes classificados como **bons** (avaliações positivas pelo usuário) entrem na análise.
2. **Matriz Binária (One-Hot Encoding)**: Transforma a tabela vertical em uma matriz pivô onde as linhas representam os usuários (`userId`) e as colunas representam os filmes (`nome_filme`).
3. **Algoritmo Apriori**: Identifica os conjuntos de itens frequentes que aparecem em pelo menos **5%** da base de dados (`min_support=0.05`).
4. **Regras de Associação**: Filtra as regras geradas exigindo uma confiança mínima de **50%** (`min_threshold=0.5`).
5. **Restrição de Antecedentes**: Para tornar o modelo viável para recomendação em produção, o script limita o gatilho inicial (antecedente) a no máximo **2 filmes**.
6. **Exportação**: O resultado final ordenado por relevância (`lift` e `confidence`) é salvo em um arquivo `.xlsx` para análise de negócios.

---

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com
cd NOME_DO_REPOSITORIO
```

### 2. Configurar o Ambiente Virtual e Instalar Dependências
```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente (Windows)
.venv\Scripts\activate

# Instalar pacotes necessários
pip install -r requirements.txt
```

### 3. Rodar o Script
Certifique-se de que o caminho do seu arquivo `ratings.xlsx` está correto no código e execute:
```bash
python Apripori_movies.py
```

---

## Métricas de Análise Utilizadas

* **Suporte (Support)**: Indica a popularidade da combinação dos filmes na base histórica de usuários.
* **Confiança (Confidence)**: Mede a precisão da regra (ex: das pessoas que assistiram ao Filme A, quantas % também gostaram do Filme B).
* **Lift**: Valida se a associação é estatisticamente real ou mera coincidência. Valores significativamente maiores que 1 indicam uma regra de recomendação forte.
