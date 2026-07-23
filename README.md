# Sistema de recomendação com A*

Projeto educacional em Python que ilustra como modelar uma recomendação de produtos como um problema de busca em grafo, utilizando o algoritmo A* (A-star).

## Como funciona

Cada produto possui:

- `nome`;
- `categoria`;
- `conversao_probabilidade`: uma estimativa de chance de conversão.

O sistema cria um grafo completo: cada produto é conectado a todos os demais. Durante a busca, a heurística prioriza produtos com maior probabilidade de conversão. Como o A* minimiza o custo, a função `heuristica` retorna o valor negativo dessa probabilidade.

O exemplo define quatro produtos, parte do **Produto A** e procura um caminho até o **Produto C**. A saída esperada é:

```text
Caminho recomendado:
Produto A (Categoria 1)
Produto B (Categoria 1)
Produto C (Categoria 2)
```

## Estrutura

| Componente | Responsabilidade |
| --- | --- |
| `Produto` | Representa um item do catálogo. |
| `AStarRecommendation` | Monta o grafo e executa a busca A*. |
| `heuristica` | Avalia a atratividade de um produto pela probabilidade de conversão. |
| `recomendacao.py` | Contém as classes, a heurística e um exemplo executável. |

## Como executar

Pré-requisito: Python 3 instalado. O projeto usa somente a biblioteca padrão (`heapq`).

```bash
python recomendacao.py
```

## Observações

Este código é uma demonstração didática, e não um recomendador de produção. Embora o grafo conecte todos os produtos diretamente, a busca pode incluir produtos intermediários conforme a prioridade definida pela heurística. Além disso, a heurística usa uma probabilidade previamente informada; um sistema real normalmente aprenderia esse valor com dados de usuários, interações e histórico de compras.

Possíveis evoluções incluem criar conexões baseadas em categorias ou comportamento de navegação, usar custos de transição reais e calcular probabilidades de conversão a partir de dados históricos.
