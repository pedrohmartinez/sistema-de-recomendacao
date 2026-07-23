import heapq # Importa o módulo heapq para usar a fila de prioridade (min-heap)

class Produto:
    """
    Representa um produto com suas características.
    """
    def __init__(self, nome, categoria, conversao_probabilidade):
        # Inicializa um produto com nome, categoria e probabilidade de conversão.
        self.nome = nome
        self.categoria = categoria
        self.conversao_probabilidade = conversao_probabilidade

    def __repr__(self):
        # Define como o objeto Produto será representado quando impresso.
        return f"{self.nome} ({self.categoria})"

class AStarRecommendation:
    """
    Implementa o sistema de recomendação de produtos usando o algoritmo A*.
    """
    def __init__(self, produtos, heuristica):
        # Inicializa o sistema com uma lista de produtos e a função heurística.
        self.produtos = produtos
        self.heuristica = heuristica  # A função heurística avalia a "qualidade" de um produto.
        self.grafo = self.criar_grafo() # Cria o grafo de conexões entre os produtos.

    def criar_grafo(self):
        """
        Cria um grafo simplificado onde cada produto se conecta a todos os outros.
        Isso simula que é possível "navegar" de qualquer produto para qualquer outro.
        """
        grafo = {}
        for produto in self.produtos:
            # Para cada produto, cria uma lista de todos os outros produtos como vizinhos.
            grafo[produto] = [p for p in self.produtos if p != produto]
        return grafo

    def a_star(self, inicio, objetivo):
        """
        Implementa o algoritmo A* para encontrar o melhor caminho entre um produto de início e um objetivo.
        """
        fila_prioridade = [] # Fila de prioridade para armazenar os nós a serem explorados (usa heapq para eficiência).
        # Adiciona o nó inicial à fila de prioridade.
        # O formato é (f_score, g_score, nó).
        # f_score = g_score + h_score (custo total estimado)
        # g_score = custo real do início até o nó atual
        # h_score = estimativa heurística do nó atual até o objetivo
        heapq.heappush(fila_prioridade, (0 + self.heuristica(inicio), 0, inicio))
        
        visitados = set() # Conjunto para armazenar os produtos já visitados e evitar loops.
        caminhos = {} # Dicionário para reconstruir o caminho: caminhos[vizinho] = produto_anterior.

        while fila_prioridade:
            # Enquanto houver produtos na fila para explorar:
            # Pega o produto com a menor f_score (maior prioridade) da fila.
            f_score, g, atual = heapq.heappop(fila_prioridade)

            if atual in visitados:
                # Se o produto já foi visitado, pula para o próximo (já encontramos um caminho melhor ou igual).
                continue

            visitados.add(atual) # Marca o produto atual como visitado.
            if atual == objetivo:
                # Se o produto atual é o objetivo, encontramos o caminho mais eficiente.
                break

            # Explora os vizinhos do produto atual.
            for vizinho in self.grafo[atual]:
                if vizinho not in visitados:
                    # Calcula a heurística para o vizinho.
                    h = self.heuristica(vizinho)
                    # Adiciona o vizinho à fila de prioridade.
                    # g + 1 é o custo real para chegar ao vizinho (g do atual + 1 passo).
                    heapq.heappush(fila_prioridade, (g + 1 + h, g + 1, vizinho))
                    # Registra que chegamos ao vizinho vindo do produto atual.
                    caminhos[vizinho] = atual

        # Recuperando o caminho do objetivo de volta ao início.
        caminho = []
        produto = objetivo
        # Percorre o dicionário 'caminhos' de trás para frente até chegar ao início.
        while produto in caminhos:
            caminho.insert(0, produto) # Insere o produto no início da lista para manter a ordem correta.
            produto = caminhos[produto] # Move para o produto anterior no caminho.
        
        # O produto inicial não é adicionado no loop acima, então o adicionamos se o caminho não estiver vazio
        # e o objetivo foi alcançado.
        if caminho and caminho[0] != inicio: # Verifica se o caminho não está vazio e se o primeiro elemento não é o início
             caminho.insert(0, inicio) # Adiciona o produto inicial ao começo do caminho
        elif not caminho and inicio == objetivo: # Caso o início e o objetivo sejam o mesmo produto
             caminho.append(inicio) # Adiciona apenas o produto inicial
        
        return caminho # Retorna a lista de produtos que formam o melhor caminho.

def heuristica(produto):
    """
    Função heurística que avalia a "atração" de um produto.
    Quanto maior a probabilidade de conversão, mais atraente é o produto.
    Retornamos o negativo da probabilidade porque o A* busca minimizar o custo total (f_score).
    Assim, produtos com alta probabilidade de conversão (ex: 0.9) terão uma heurística de -0.9,
    o que os torna "mais baratos" e, portanto, mais prioritários.
    """
    return -produto.conversao_probabilidade

# --- Exemplo de Uso do Sistema de Recomendação ---

# 1. Definindo os produtos disponíveis.
produtos = [
    Produto("Produto A", "Categoria 1", 0.9), # Alta probabilidade de conversão
    Produto("Produto B", "Categoria 1", 0.8),
    Produto("Produto C", "Categoria 2", 0.7),
    Produto("Produto D", "Categoria 2", 0.6), # Baixa probabilidade de conversão
]

# 2. Criando o sistema de recomendação, passando os produtos e a função heurística.
recomendador = AStarRecommendation(produtos, heuristica)

# 3. Definindo o produto de início e o produto objetivo para a busca.
inicio = produtos[0]  # Produto A
objetivo = produtos[2]  # Produto C

# 4. Executando o algoritmo A* para encontrar o melhor caminho.
caminho_recomendado = recomendador.a_star(inicio, objetivo)

# 5. Exibindo o caminho de produtos recomendado.
print("Caminho recomendado:")
if caminho_recomendado:
    for p in caminho_recomendado:
        print(p)
else:
    print("Nenhum caminho encontrado.")

