# Análises de Desempenho de Livros

## 1. Performance dos Livros
- **Tabelas Relacionadas:** book, sales, ratings, publisher 
- **Insights:**
  - Identificar os livros mais vendidos e bem avaliados para determinar quais gêneros ou autores têm maior apelo.  -OK
  - Cruzar as vendas e avaliações por editoras para avaliar o desempenho dos editores.                             -OK
  - Analisar se há correlação entre boas avaliações (ratings) e altos volumes de vendas (sales).                   -OK

## 2. Tendências por Gênero
- **Tabelas Relacionadas:** genders, sales, ratings
- **Insights:**
  - Descobrir quais gêneros literários estão crescendo em popularidade com base em vendas e avaliações.                 -POSTERIOR
  - Determinar os gêneros mais rentáveis para priorizar investimentos em marketing e estoque.                           -OK
  - Verificar quais gêneros/formato têm alta avaliação, mas baixo volume de vendas, para estratégias promocionais específicas.  -A REALIZAR

## 3. Desempenho por Autor
- **Tabelas Relacionadas:** author, book, sales, ratings, award
- **Insights:**
  - Analisar quais autores têm maior volume de vendas e melhores avaliações.
  - Identificar se autores premiados (award) têm impacto significativo nas vendas.
  - Verificar a consistência do desempenho de autores que possuem séries de livros.

## 4. Efeito de Séries de Livros
- **Tabelas Relacionadas:** series, book, sales, ratings
- **Insights:**
  - Avaliar se séries de livros geram maior engajamento e vendas em relação a livros únicos.
  - Analisar o desempenho de vendas ao longo de uma série, identificando padrões (ex.: queda de interesse ao longo de volumes ou aumento de vendas com o lançamento de novos volumes).

## 5. Impacto do Formato na Venda e na Avaliação
- **Tabelas Relacionadas:** format, sales, ratings
- **Insights:**
  - Descobrir quais formatos (e.g., físico, e-book, audiobook) têm melhor desempenho em vendas e avaliações.
  - Analisar diferenças regionais ou demográficas no consumo de formatos específicos.

## 6. Eficácia de Editoras
- **Tabelas Relacionadas:** publisher, sales, ratings
- **Insights:**
  - Avaliar quais editoras consistentemente publicam livros de alta performance.
  - Verificar se há padrões nas editoras que focam em gêneros específicos e seu impacto no mercado.

## 7. Efeitos de Premiações
- **Tabelas Relacionadas:** award, sales, ratings
- **Insights:**
  - Analisar o impacto de prêmios literários nas vendas e avaliações de livros.
  - Verificar a longevidade do impacto de prêmios (ex.: vendas aumentam por quanto tempo após ganhar um prêmio?).

## 8. Perfil dos Melhores Livros
- **Tabelas Relacionadas:** Todas
- **Insights:**
  - Criar um “perfil do sucesso”, analisando características comuns entre os livros mais vendidos e bem avaliados (ex.: gênero, formato, premiação, editora, autor).
  - Determinar combinações de fatores que mais contribuem para o sucesso de um livro (ex.: autor premiado em gêneros populares, publicado por uma editora de alto desempenho).

## 9. Previsão de Desempenho
- **Tabelas Relacionadas:** sales, ratings, author, genders
- **Insights:**
  - Construir modelos preditivos para estimar vendas futuras com base em gênero, avaliação, formato e autor.
  - Identificar livros promissores antes de serem lançados, utilizando dados históricos.

## 10. Otimização de Estoque e Marketing
- **Tabelas Relacionadas:** sales, ratings, info, book, genders
- **Insights:**
  - Prever demanda com base em tendências de vendas e avaliações por região e gênero.
  - Identificar produtos de baixo desempenho para reduzir desperdícios.
  - Melhorar estratégias de marketing, direcionando campanhas para públicos que demonstraram maior interesse em certos gêneros, autores ou formatos.
