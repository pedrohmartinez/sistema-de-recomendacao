# 1. Criando a Rede Bayesiana
probabilidades = {
    "HistoricoCompras": {0: 0.7, 1: 0.3},  # Prob. de ter (1) ou não (0) histórico de compras
    "TempoNoSite": {0: 0.6, 1: 0.4},       # Prob. de passar pouco (0) ou muito (1) tempo no site
    "ClicouEmPromocao": {0: 0.8, 1: 0.2},  # Prob. de não (0) ou sim (1) clicar em promoção
    "Compra": {
        (0, 0, 0): 0.1,  # Prob. de compra para cada combinação de histórico, tempo e promoção
        (0, 0, 1): 0.3,
        (0, 1, 0): 0.2,
        (0, 1, 1): 0.6,
        (1, 0, 0): 0.4,
        (1, 0, 1): 0.7,
        (1, 1, 0): 0.8,
        (1, 1, 1): 0.9
    }
}

# 2. Função para calcular a probabilidade conjunta de compra
def calcular_probabilidade_compra(evidencias):
    historico = evidencias["HistoricoCompras"]  # Obtém o valor do histórico de compras
    tempo = evidencias["TempoNoSite"]           # Obtém o valor do tempo no site
    promocao = evidencias["ClicouEmPromocao"]  # Obtém o valor da interação com promoção

    # Busca a probabilidade de compra na tabela "Compra" com base nas evidências
    prob_compra = probabilidades["Compra"][(historico, tempo, promocao)]
    prob_nao_compra = 1 - prob_compra           # Calcula a probabilidade de não compra

    return {"Comprar": prob_compra, "Não Comprar": prob_nao_compra} # Retorna as probabilidades

# 3. Testando com o cenário descrito
evidencias = {
    "HistoricoCompras": 1,  # Cliente tem histórico de compras
    "TempoNoSite": 0,       # Cliente passou pouco tempo no site
    "ClicouEmPromocao": 1   # Cliente clicou em promoções
}

resultados = calcular_probabilidade_compra(evidencias) # Chama a função com as evidências
print("Probabilidades de Compra:")
for resultado, probabilidade in resultados.items(): # Itera e imprime os resultados
    print(f"{resultado}: {probabilidade:.2f}")
