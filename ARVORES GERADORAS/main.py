import json
from grafo import Grafo
from prim import AlgoritmoPrim
from kruskal import AlgoritmoKruskal

def carregar_grafos_do_arquivo(caminho):
    """Carrega os grafos a partir de um arquivo JSON."""
    with open(caminho, 'r') as arquivo:
        return json.load(arquivo)

def main():
    # Carregar os dados dos grafos do arquivo JSON
    dados_grafos = carregar_grafos_do_arquivo('Grafo.json')

    # Criar instâncias dos grafos
    g1 = Grafo(dados_grafos["grafo1"]["nos"], dados_grafos["grafo1"]["arestas"])
    g2 = Grafo(dados_grafos["grafo2"]["nos"], dados_grafos["grafo2"]["arestas"])

    # Executar o algoritmo de Prim
    prim1 = AlgoritmoPrim(g1)
    prim2 = AlgoritmoPrim(g2)

    # Encontrar a Árvore Geradora Mínima para cada grafo
    agm1 = prim1.encontrar_arvore_geradora_minima()
    agm2 = prim2.encontrar_arvore_geradora_minima()

    # Executar o algoritmo de Kruskal
    kruskal1 = AlgoritmoKruskal(g1)
    kruskal2 = AlgoritmoKruskal(g2)
    
    # Encontrar a Árvore Geradora Mínima para cada grafo usando Kruskal
    agm1_kruskal = kruskal1.encontrar_arvore_geradora_minima()
    agm2_kruskal = kruskal2.encontrar_arvore_geradora_minima()

    # Mostrar os resultados
    print("Árvore Geradora Mínima para o Grafo 1 (Prim):")
    for origem, destino, peso in agm1:
        print(f"Origem: {origem}, Destino: {destino}, Peso: {peso}")

    print("\nÁrvore Geradora Mínima para o Grafo 2 (Prim):")
    for origem, destino, peso in agm2:
        print(f"Origem: {origem}, Destino: {destino}, Peso: {peso}")
        
    # Mostrar os resultados para Kruskal
    print("\nÁrvore Geradora Mínima para o Grafo 1 (Kruskal):")
    for origem, destino, peso in agm1_kruskal:
        print(f"Origem: {origem}, Destino: {destino}, Peso: {peso}")

    print("\nÁrvore Geradora Mínima para o Grafo 2 (Kruskal):")
    for origem, destino, peso in agm2_kruskal:
        print(f"Origem: {origem}, Destino: {destino}, Peso: {peso}")
        
if __name__ == "__main__":
    main()
