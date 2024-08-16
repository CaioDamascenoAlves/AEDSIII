import os
import glob
import timeit
import json
from maze import Maze
from bfs_solver import BFSSolver
from dfs_solver import DFSSolver

def criar_pastas():
    """Cria as pastas DFS e BFS se não existirem."""
    if not os.path.exists('DFS'):
        os.makedirs('DFS')
    if not os.path.exists('BFS'):
        os.makedirs('BFS')

def salvar_solucao(caminho, nome_arquivo, tipo):
    """Salva a solução em um arquivo JSON."""
    pasta = 'DFS' if tipo == 'DFS' else 'BFS'
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    with open(caminho_arquivo, 'w') as f:
        json.dump(caminho, f)

def processar_labirinto(arquivo):
    try:
        labirinto = Maze(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado. Pulando...")
        return

    inicio = labirinto.encontrar_ponto('S')
    fim = labirinto.encontrar_ponto('E')

    if not inicio or not fim:
        print(f"Arquivo de labirinto {arquivo} inválido. Pulando...")
        return

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

    print(f"\nArquivo: {arquivo}")
    print("\nBFS:")
    if caminho_bfs:
        print("Caminho:", ' '.join(map(str, caminho_bfs)))
        salvar_solucao(caminho_bfs, os.path.basename(arquivo).replace('.txt', '.json'), 'BFS')
    else:
        print("Caminho não encontrado.")
    print("Tempo:", tempo_bfs, "s")

    print("\nDFS:")
    if caminho_dfs:
        print("Caminho:", ' '.join(map(str, caminho_dfs)))
        salvar_solucao(caminho_dfs, os.path.basename(arquivo).replace('.txt', '.json'), 'DFS')
    else:
        print("Caminho não encontrado.")
    print("Tempo:", tempo_dfs, "s")

    print("\nDiferença de Tempo (BFS - DFS):", diferenca_tempo, "s")

def main():
    criar_pastas()
    diretorio = input("Informe o diretório com os arquivos .txt: ")
    arquivos_txt = glob.glob(os.path.join(diretorio, "*.txt"))

    if not arquivos_txt:
        print("Nenhum arquivo .txt encontrado no diretório especificado.")
        return

    for arquivo in arquivos_txt:
        processar_labirinto(arquivo)

if __name__ == "__main__":
    main()
