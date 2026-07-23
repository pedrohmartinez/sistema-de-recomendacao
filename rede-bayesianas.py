# 1. Criando a Rede Bayesiana
# Este dicionário 'probabilidades' representa nossa Rede Bayesiana.
# Ele armazena as probabilidades de cada evento e as probabilidades condicionais.
probabilidades = {
    # Probabilidades da variável "HistoricoCompras":
    # 0: Cliente NÃO tem histórico de compras (70% de chance)
    # 1: Cliente TEM histórico de compras (30% de chance)
    "HistoricoCompras": {0: 0.7, 1: 0.3},

    # Probabilidades da variável "TempoNoSite":
    # 0: Cliente passou POUCO tempo no site (60% de chance)
    # 1: Cliente passou MUITO tempo no site (40% de chance)
    "TempoNoSite": {0: 0.6, 1: 0.4},

    # Probabilidades da variável "ClicouEmPromocao":
    # 0: Cliente NÃO clicou em promoção (80% de chance)
    # 1: Cliente CLICOU em promoção (20% de chance)
    "ClicouEmPromocao": {0: 0.8, 1: 0.2},

    # Probabilidades condicionais da variável "Compra":
    # Aqui, a probabilidade de compra depende da combinação das outras três variáveis.
    # As chaves são tuplas (HistoricoCompras, TempoNoSite, ClicouEmPromocao).
    "Compra": {
        (0, 0, 0): 0.1,  # Prob. de compra se: Não tem histórico, pouco tempo, não clicou
        (0, 0, 1): 0.3,  # Prob. de compra se: Não tem histórico, pouco tempo, clicou
        (0, 1, 0): 0.2,  # Prob. de compra se: Não tem histórico, muito tempo, não clicou
        (0, 1, 1): 0.6,  # Prob. de compra se: Não tem histórico, muito tempo, clicou
        (1, 0, 0): 0.4,  # Prob. de compra se: Tem histórico, pouco tempo, não clicou
        (1, 0, 1): 0.7,  # Prob. de compra se: Tem histórico, pouco tempo, clicou
        (1, 1, 0): 0.8,  # Prob. de compra se: Tem histórico, muito tempo, não clicou
        (1, 1, 1): 0.9   # Prob. de compra se: Tem histórico, muito tempo, clicou
    }
}

# 2. Função para calcular a probabilidade conjunta de compra
# Esta função recebe as "evidências" (o comportamento do cliente)
# e calcula a probabilidade de ele realizar uma compra.
def calcular_probabilidade_compra(evidencias):
    # Extrai o valor do histórico de compras das evidências fornecidas.
    historico = evidencias["HistoricoCompras"]
    # Extrai o valor do tempo no site das evidências fornecidas.
    tempo = evidencias["TempoNoSite"]
    # Extrai o valor da interação com promoções das evidências fornecidas.
    promocao = evidencias["ClicouEmPromocao"]

    # Busca no dicionário 'probabilidades' a probabilidade de compra
    # correspondente à combinação específica de histórico, tempo e promoção.
    prob_compra = probabilidades["Compra"][(historico, tempo, promocao)]

    # Calcula a probabilidade de NÃO compra, que é o complemento da probabilidade de compra.
    prob_nao_compra = 1 - prob_compra

    # Retorna um dicionário com as duas probabilidades calculadas.
    return {"Comprar": prob_compra, "Não Comprar": prob_nao_compra}

# 3. Testando com o cenário descrito
# Definimos um cenário específico de um cliente para testar nosso modelo.
evidencias = {
    "HistoricoCompras": 1,  # O cliente TEM histórico de compras.
    "TempoNoSite": 0,       # O cliente passou POUCO tempo no site.
    "ClicouEmPromocao": 1   # O cliente CLICOU em promoções.
}

# Chamamos a função para calcular as probabilidades de compra para este cliente.
resultados = calcular_probabilidade_compra(evidencias)

# Imprime o cabeçalho dos resultados.
print("Probabilidades de Compra:")
# Itera sobre os resultados e imprime cada probabilidade formatada.
for resultado, probabilidade in resultados.items():
    print(f"{resultado}: {probabilidade:.2f}")
