# Exemplos de IA para recomendação

Projeto educacional em Python com dois exemplos de técnicas de Inteligência Artificial aplicadas ao contexto de recomendação e conversão de produtos:

- busca em grafo com o algoritmo A*;
- estimativa de compra por uma rede bayesiana simplificada.

O projeto não requer bibliotecas externas.

## Arquivos

| Arquivo | Descrição |
| --- | --- |
| `recomendacao.py` | Recomenda produtos por meio de uma busca A*. |
| `rede-bayesianas.py` | Calcula a probabilidade de compra a partir de evidências do comportamento do cliente. |

## Recomendação com A*

O arquivo `recomendacao.py` representa cada item por meio da classe `Produto`, contendo nome, categoria e probabilidade de conversão. A classe `AStarRecommendation` cria um grafo em que todos os produtos são vizinhos e executa a busca A* entre um produto inicial e um objetivo.

A heurística retorna o negativo da probabilidade de conversão. Isso faz com que produtos com maior chance de conversão tenham prioridade, pois o A* busca o menor custo estimado.

Execute com:

```bash
python recomendacao.py
```

No exemplo incluído, a busca parte do Produto A até o Produto C.

## Rede bayesiana simplificada

O arquivo `rede-bayesianas.py` usa uma tabela de probabilidades para estimar se um cliente comprará ou não. A decisão considera três evidências binárias:

| Evidência | `0` | `1` |
| --- | --- | --- |
| `HistoricoCompras` | Não possui histórico de compras | Possui histórico de compras |
| `TempoNoSite` | Permaneceu pouco tempo | Permaneceu muito tempo |
| `ClicouEmPromocao` | Não clicou em promoção | Clicou em promoção |

A função `calcular_probabilidade_compra(evidencias)` consulta a probabilidade de compra associada à combinação das evidências e retorna também a probabilidade complementar de não comprar.

O cenário de exemplo representa um cliente que possui histórico de compras, ficou pouco tempo no site e clicou em uma promoção. O resultado é:

```text
Probabilidades de Compra:
Comprar: 0.70
Não Comprar: 0.30
```

Execute com:

```bash
python rede-bayesianas.py
```

## Observações

Os dois scripts são demonstrações didáticas. As probabilidades são definidas manualmente e a rede bayesiana é representada por uma tabela de consulta, sem treinamento estatístico. Em um sistema real, os valores poderiam ser estimados a partir de dados históricos, e as conexões entre produtos poderiam refletir categorias, navegação e interações reais dos usuários.
