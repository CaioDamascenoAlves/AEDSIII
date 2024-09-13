from collections import defaultdict

# Algoritmo de Ford-Fulkerson
class FordFulkerson:
    # Método construtor, inicializa o grafo e o grafo residual
    def __init__(self, graph):
        self.graph = graph  # Grafo original com as capacidades das arestas
        # Grafo residual que será usado para armazenar a capacidade remanescente
        self.residual_graph = defaultdict(dict)

    # Função que realiza a busca em largura (BFS) no grafo residual
    def bfs(self, source, sink, parent):
        visited = set()  # Conjunto de nós visitados para evitar ciclos
        queue = [source]  # Fila de nós para explorar, começando pela fonte
        visited.add(source)  # Marca o nó fonte como visitado

        # Loop enquanto houver nós na fila
        while queue:
            u = queue.pop(0)  # Retira o nó da frente da fila
            # Explora todos os nós adjacentes ao nó atual no grafo residual
            for v in self.residual_graph[u]:
                # Se o nó ainda não foi visitado e há capacidade residual na aresta
                if v not in visited and self.residual_graph[u][v] > 0:
                    queue.append(v)  # Adiciona o nó à fila para explorar
                    visited.add(v)  # Marca o nó como visitado
                    parent[v] = u  # Armazena o caminho, dizendo que v foi visitado a partir de u
                    # Se o nó de destino (sink) foi alcançado, retorna True
                    if v == sink:
                        return True
        return False  # Retorna False se o caminho do source ao sink não for encontrado

    # Função principal que executa o algoritmo de Ford-Fulkerson
    def ford_fulkerson(self, source, sink):
        max_flow = 0  # Inicializa o fluxo máximo com 0
        parent = {}  # Dicionário para armazenar o caminho encontrado no BFS

        # Inicializa o grafo residual com as capacidades do grafo original
        for edge in self.graph['edges']:
            self.residual_graph[edge['source']][edge['target']] = edge['weight']

        # Continua enquanto houver um caminho do source ao sink encontrado pelo BFS
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')  # Inicializa o fluxo do caminho encontrado como infinito
            s = sink  # Começa do nó de destino (sink)

            # Encontra o fluxo mínimo ao longo do caminho encontrado
            while s != source:
                path_flow = min(path_flow, self.residual_graph[parent[s]][s])  # Atualiza o fluxo mínimo
                s = parent[s]  # Vai para o nó anterior no caminho

            max_flow += path_flow  # Adiciona o fluxo mínimo encontrado ao fluxo máximo total

            # Atualiza o grafo residual: subtrai o fluxo mínimo nas arestas do caminho e
            # adiciona o fluxo inverso para permitir fluxos "de volta" se necessário
            v = sink
            while v != source:
                u = parent[v]  # Obtém o nó anterior no caminho
                self.residual_graph[u][v] -= path_flow  # Diminui o fluxo da capacidade residual
                # Aumenta o fluxo inverso no grafo residual (se não existir, inicializa com 0)
                self.residual_graph[v][u] = self.residual_graph.get(v, {}).get(u, 0) + path_flow
                v = parent[v]  # Move para o próximo nó no caminho

        return max_flow  # Retorna o valor total do fluxo máximo encontrado
