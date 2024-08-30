class Grafo:
    def __init__(self, nos, arestas):
        self.nos = nos
        self.arestas = arestas
        self.adjacencias = {no: [] for no in nos}
        self._construir_grafo()

    def _construir_grafo(self):
        """Constrói a lista de adjacência a partir das arestas."""
        for aresta in self.arestas:
            origem = aresta["origem"]
            destino = aresta["destino"]
            peso = aresta["peso"]
            self.adjacencias[origem].append((destino, peso))
            self.adjacencias[destino].append((origem, peso))