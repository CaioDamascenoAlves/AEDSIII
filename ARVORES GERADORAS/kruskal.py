from unionFind import UnionFind

class AlgoritmoKruskal:
    def __init__(self, grafo):
        self.grafo = grafo

    def encontrar_arvore_geradora_minima(self):
        """Encontra a Árvore Geradora Mínima (AGM) usando o algoritmo de Kruskal."""
        agm = []
        # Ordena as arestas pelo peso
        arestas = sorted(self.grafo.arestas, key=lambda aresta: aresta['peso'])

        # Inicializa a estrutura Union-Find para controle dos ciclos
        uf = UnionFind(len(self.grafo.nos))
        indice_no = {no: i for i, no in enumerate(self.grafo.nos)}

        for aresta in arestas:
            origem = aresta['origem']
            destino = aresta['destino']
            peso = aresta['peso']

            # Obtenha o índice dos nós para o Union-Find
            u = indice_no[origem]
            v = indice_no[destino]

            # Verifica se a aresta cria um ciclo
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                agm.append((origem, destino, peso))

        return agm