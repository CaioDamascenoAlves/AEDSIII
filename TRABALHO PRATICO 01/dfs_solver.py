class DFSSolver:
    def __init__(self, maze):
        self.maze = maze.get_labirinto()

    def encontrar_caminho(self, inicio, fim):
        pilha = [(inicio, [inicio])]
        visitados = set()
        
        while pilha:
            (atual, caminho) = pilha.pop()
            
            if atual in visitados:
                continue
            
            visitados.add(atual)
            
            if atual == fim:
                return caminho
            
            x, y = atual
            vizinhos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            
            for nx, ny in vizinhos:
                if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]):
                    if self.maze[nx][ny] != '#' and (nx, ny) not in visitados:
                        pilha.append(((nx, ny), caminho + [(nx, ny)]))
        
        return None
