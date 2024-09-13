from collections import defaultdict

# Algoritmo de Sucessivos Caminhos Mínimos
class SuccessiveShortestPaths:
    # Método construtor que inicializa o grafo e os grafos residual e de custo
    def __init__(self, graph):
        self.graph = graph  # Grafo original com capacidade e custos nas arestas
        # Grafo residual que será usado para armazenar a capacidade remanescente
        self.residual_graph = defaultdict(lambda: defaultdict(int))
        # Grafo de custos que será usado para armazenar o custo de cada aresta
        self.cost_graph = defaultdict(lambda: defaultdict(int))

    # Função que implementa o algoritmo de Bellman-Ford para encontrar o caminho de custo mínimo
    def bellman_ford(self, source):
        # Inicializa todas as distâncias como infinito (Inf)
        distances = defaultdict(lambda: float('Inf'))
        parent = {}  # Dicionário que armazena o caminho percorrido
        distances[source] = 0  # A distância do nó fonte (source) até ele mesmo é 0

        # Relaxa as arestas repetidamente (n-1 vezes, onde n é o número de nós)
        for _ in range(len(self.graph['nodes']) - 1):
            # Itera sobre todas as arestas do grafo
            for edge in self.graph['edges']:
                u, v = edge['source'], edge['target']  # Nó de origem e de destino
                capacity = self.residual_graph[u][v]  # Capacidade residual da aresta
                cost = self.cost_graph[u][v]  # Custo da aresta
                # Se houver capacidade e o custo do caminho via u for menor que a distância atual até v
                if capacity > 0 and distances[u] + cost < distances[v]:
                    distances[v] = distances[u] + cost  # Atualiza a distância mínima para v
                    parent[v] = u  # Atualiza o caminho para v, dizendo que v foi alcançado via u

        return distances, parent  # Retorna as distâncias mínimas e o caminho percorrido

    # Função principal que executa o algoritmo de Sucessivos Caminhos Mínimos
    def successive_shortest_paths(self, source, sink):
        max_flow = 0  # Inicializa o fluxo máximo com 0
        min_cost = 0  # Inicializa o custo mínimo com 0

        # Inicializa o grafo residual e o grafo de custos com os valores do grafo original
        for edge in self.graph['edges']:
            self.residual_graph[edge['source']][edge['target']] = edge['capacity']  # Capacidade
            self.cost_graph[edge['source']][edge['target']] = edge['cost']  # Custo

        while True:
            # Executa o algoritmo de Bellman-Ford para encontrar o caminho de custo mínimo
            distances, parent = self.bellman_ford(source)

            # Se não houver caminho disponível para o nó de destino (sink), termina o loop
            if distances[sink] == float('Inf'):
                break  # Caminho não encontrado

            # Encontra o fluxo máximo possível ao longo do caminho de custo mínimo encontrado
            path_flow = float('Inf')  # Inicializa o fluxo do caminho como infinito
            v = sink  # Começa do nó de destino (sink)

            # Percorre o caminho encontrado do sink até o source para calcular o fluxo máximo
            while v != source:
                u = parent[v]  # Obtém o nó anterior no caminho
                # Atualiza o fluxo mínimo ao longo do caminho
                path_flow = min(path_flow, self.residual_graph[u][v])
                v = parent[v]  # Vai para o próximo nó no caminho

            max_flow += path_flow  # Adiciona o fluxo máximo possível ao fluxo total

            # Atualiza as capacidades residuais e calcula o custo total do caminho
            v = sink
            while v != source:
                u = parent[v]  # Obtém o nó anterior no caminho
                # Diminui o fluxo usado da capacidade residual
                self.residual_graph[u][v] -= path_flow
                # Aumenta o fluxo na direção oposta no grafo residual (para permitir fluxos reversos)
                self.residual_graph[v][u] += path_flow
                # Adiciona o custo do caminho ao custo total
                min_cost += path_flow * self.cost_graph[u][v]
                v = parent[v]  # Move para o próximo nó no caminho

        return max_flow, min_cost  # Retorna o fluxo máximo e o custo mínimo