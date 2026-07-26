class BaseDeConhecimento:
    def __init__(self):
        # Inicializa a lista de fatos (informações conhecidas)
        self.fatos = []
        # Inicializa a lista de regras (condições e conclusões)
        self.regras = []

    def adicionar_fato(self, fato):
        # Método para adicionar um novo fato à base de conhecimento
        self.fatos.append(fato)

    def adicionar_regra(self, condicao, conclusao):
        # Método para adicionar uma nova regra.
        # Uma regra é uma tupla onde 'condicao' é uma lista de fatos necessários
        # e 'conclusao' é o fato que pode ser inferido.
        self.regras.append((condicao, conclusao))

class SistemaEspecialista:
    def __init__(self, base_conhecimento):
        # O sistema especialista recebe uma instância da BaseDeConhecimento
        self.base_conhecimento = base_conhecimento

    def inferir(self):
        # Loop principal de inferência. Continua enquanto novos fatos são descobertos.
        novos_fatos = True
        while novos_fatos:
            novos_fatos = False # Assume que nenhum novo fato será encontrado nesta iteração
            # Itera sobre todas as regras na base de conhecimento
            for condicao, conclusao in self.base_conhecimento.regras:
                # Verifica se TODOS os fatos na 'condicao' da regra já estão na base de fatos
                if all(fato in self.base_conhecimento.fatos for fato in condicao):
                    # Se a condição é verdadeira, verifica se a 'conclusao' já não é um fato conhecido
                    if conclusao not in self.base_conhecimento.fatos:
                        # Se a conclusão não é um fato, adiciona-a à base de fatos
                        self.base_conhecimento.fatos.append(conclusao)
                        novos_fatos = True # Indica que um novo fato foi encontrado, então o loop deve continuar

# --- Exemplo de Uso ---

# Criando uma instância da Base de Conhecimento
base = BaseDeConhecimento()

# Adicionando fatos iniciais (sintomas do paciente)
base.adicionar_fato("febre alta")
base.adicionar_fato("tosse")
# base.adicionar_fato("dificuldade para respirar") # Descomente para testar a pneumonia

# Adicionando regras de diagnóstico
base.adicionar_regra(["febre alta", "tosse"], "infecção respiratória")
base.adicionar_regra(["infecção respiratória", "dificuldade para respirar"], "pneumonia")

# Criando uma instância do Sistema Especialista, passando a base de conhecimento
sistema = SistemaEspecialista(base)

# Executando o processo de inferência para deduzir novos fatos/diagnósticos
sistema.inferir()

# Exibindo todos os fatos conhecidos após a inferência (incluindo os diagnósticos)
print("Fatos inferidos:")
print(base.fatos)