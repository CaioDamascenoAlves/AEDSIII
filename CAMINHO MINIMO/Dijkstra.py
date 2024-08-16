import heapq

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def calcular_menor_caminho(self, inicio):
        distancias = {no: float('infinity') for no in self.grafo.arestas}
        distancias[inicio] = 0
        
        fila_prioridade = [(0, inicio)]
        
        while fila_prioridade:
            distancia_atual, no_atual = heapq.heappop(fila_prioridade)
            
            if distancia_atual > distancias[no_atual]:
                continue
            
            for vizinho, peso in self.grafo.arestas.get(no_atual, []):
                distancia = distancia_atual + peso
                
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(fila_prioridade, (distancia, vizinho))
        
        return distancias
