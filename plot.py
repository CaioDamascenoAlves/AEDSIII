import os
import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def rotacionar_90_graus_direita(pos):
    """Rotaciona as coordenadas dos nós 90 graus para a direita."""
    return {n: (p[1], -p[0]) for n, p in pos.items()}

def criar_arquivo_html(caminho_json, tipo):
    """Cria um arquivo HTML para visualizar o grafo a partir de um arquivo JSON."""
    nome_arquivo = os.path.basename(caminho_json).replace('.json', '.png')
    caminho_png = os.path.join(tipo, nome_arquivo)

    # Carregar dados do arquivo JSON
    with open(caminho_json, 'r') as f:
        dados = json.load(f)

    # Criar um grafo com networkx
    G = nx.Graph()

    # Adicionar nós
    for i, coordenada in enumerate(dados):
        G.add_node(i, pos=coordenada)

    # Adicionar arestas entre nós consecutivos
    for i in range(len(dados) - 1):
        G.add_edge(i, i + 1)

    # Obter posições dos nós e rotacionar
    pos = nx.get_node_attributes(G, 'pos')
    pos_rotacionado = rotacionar_90_graus_direita(pos)

    # Desenhar o grafo usando matplotlib
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos_rotacionado, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10, font_color='black', width=2)
    plt.title('Grafo Gerado a partir do JSON')

    # Salvar como imagem PNG
    plt.savefig(caminho_png)
    plt.close()

    # Criar arquivo HTML com a imagem PNG
    caminho_html = os.path.join(tipo, os.path.basename(caminho_json).replace('.json', '.html'))
    with open(caminho_html, 'w') as f:
        f.write(f'<html><body><h1>Grafo Gerado a partir do JSON</h1><img src="{nome_arquivo}" alt="Grafo"/></body></html>')

    print(f"Arquivo HTML gerado para {caminho_json} em {tipo}/")

def processar_pastas():
    """Processa as pastas DFS e BFS para criar arquivos HTML."""
    for tipo in ['DFS', 'BFS']:
        pasta = tipo
        if not os.path.exists(pasta):
            print(f"Pasta {pasta} não encontrada.")
            continue

        arquivos_json = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.json')]

        if not arquivos_json:
            print(f"Nenhum arquivo JSON encontrado na pasta {pasta}.")
            continue

        for arquivo_json in arquivos_json:
            criar_arquivo_html(arquivo_json, tipo)

if __name__ == "__main__":
    processar_pastas()
