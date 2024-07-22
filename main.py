import timeit
from maze import Maze
from bfs_solver import BFSSolver
from dfs_solver import DFSSolver

def main():
    while True:
        arquivo = input("Informe o arquivo (0 para sair): ")
        if arquivo == '0':
            break

        try:
            labirinto = Maze(arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado. Tente novamente.")
            continue
        
        inicio = labirinto.encontrar_ponto('S')
        fim = labirinto.encontrar_ponto('E')

        if not inicio or not fim:
            print("Arquivo de labirinto inválido.")
            continue

        solver_bfs = BFSSolver(labirinto)
        solver_dfs = DFSSolver(labirinto)

        inicio_tempo_bfs = timeit.default_timer()
        caminho_bfs = solver_bfs.encontrar_caminho(inicio, fim)
        fim_tempo_bfs = timeit.default_timer()

        inicio_tempo_dfs = timeit.default_timer()
        caminho_dfs = solver_dfs.encontrar_caminho(inicio, fim)
        fim_tempo_dfs = timeit.default_timer()

        tempo_bfs = fim_tempo_bfs - inicio_tempo_bfs
        tempo_dfs = fim_tempo_dfs - inicio_tempo_dfs
        diferenca_tempo = abs(tempo_bfs - tempo_dfs)

        print("\nBFS:")
        if caminho_bfs:
            print("Caminho:", ' '.join(map(str, caminho_bfs)))
        else:
            print("Caminho não encontrado.")
        print("Tempo:", tempo_bfs, "s")

        print("\nDFS:")
        if caminho_dfs:
            print("Caminho:", ' '.join(map(str, caminho_dfs)))
        else:
            print("Caminho não encontrado.")
        print("Tempo:", tempo_dfs, "s")

        print("\nDiferença de Tempo (BFS - DFS):", diferenca_tempo, "s")

if __name__ == "__main__":
    main()
