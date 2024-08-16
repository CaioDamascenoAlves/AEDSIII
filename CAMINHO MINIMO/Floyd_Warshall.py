class FloydWarshall:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def calcular_todos_caminhos_minimos(self):
        # Inicializando a matriz de distâncias
        distancias = {}
        for origem in self.grafo.arestas:
            distancias[origem] = {}
            for destino in self.grafo.arestas:
                if origem == destino:
                    distancias[origem][destino] = 0
                else:
                    distancias[origem][destino] = float('infinity')
            for destino, peso in self.grafo.arestas[origem]:
                distancias[origem][destino] = peso

        # Algoritmo Floyd-Warshall
        for k in self.grafo.arestas:
            for i in self.grafo.arestas:
                for j in self.grafo.arestas:
                    if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                        distancias[i][j] = distancias[i][k] + distancias[k][j]

        return distancias
