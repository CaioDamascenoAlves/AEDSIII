class AlgoritmoPrim:
    def __init__(self, grafo):
        self.grafo = grafo

    def encontrar_arvore_geradora_minima(self):
        """Encontra a Árvore Geradora Mínima (AGM) usando o algoritmo de Prim."""
        nos_visitados = set()
        arestas_agm = []
        nos = list(self.grafo.nos)
        no_inicial = nos[0]
        nos_visitados.add(no_inicial)
        arestas_possiveis = [(no_inicial, destino, peso) for destino, peso in self.grafo.adjacencias[no_inicial]]

        while arestas_possiveis:
            arestas_possiveis.sort(key=lambda x: x[2])  # Ordena com base no peso
            menor_aresta = arestas_possiveis.pop(0)
            origem, destino, peso = menor_aresta

            if destino not in nos_visitados:
                nos_visitados.add(destino)
                arestas_agm.append((origem, destino, peso))

                for proxima_aresta in self.grafo.adjacencias[destino]:
                    if proxima_aresta[0] not in nos_visitados:
                        arestas_possiveis.append((destino, proxima_aresta[0], proxima_aresta[1]))

        return arestas_agm
