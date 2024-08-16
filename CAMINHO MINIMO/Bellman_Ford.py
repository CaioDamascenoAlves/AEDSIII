class BellmanFord:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def calcular_menor_caminho(self, inicio):
        distancias = {no: float('infinity') for no in self.grafo.arestas}
        distancias[inicio] = 0
        
        for _ in range(len(self.grafo.arestas) - 1):
            for origem in self.grafo.arestas:
                for destino, peso in self.grafo.arestas[origem]:
                    if distancias[origem] + peso < distancias[destino]:
                        distancias[destino] = distancias[origem] + peso

        # Verifica se há ciclos de peso negativo
        for origem in self.grafo.arestas:
            for destino, peso in self.grafo.arestas[origem]:
                if distancias[origem] + peso < distancias[destino]:
                    raise ValueError("Grafo contém ciclo de peso negativo")
        
        return distancias
