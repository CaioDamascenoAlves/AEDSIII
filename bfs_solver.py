from collections import deque

class BFSSolver:
    def __init__(self, maze):
        self.maze = maze.get_labirinto()

    def encontrar_caminho(self, inicio, fim):
        filas = deque([inicio])
        caminhos = {inicio: [inicio]}
        
        while filas:
            atual = filas.popleft()
            if atual == fim:
                return caminhos[atual]
            
            x, y = atual
            vizinhos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            
            for nx, ny in vizinhos:
                if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]):
                    if self.maze[nx][ny] != '#' and (nx, ny) not in caminhos:
                        filas.append((nx, ny))
                        caminhos[(nx, ny)] = caminhos[atual] + [(nx, ny)]
        
        return None
