import json
from FordFulkerson import FordFulkerson
from SuccessiveShortestPaths import SuccessiveShortestPaths

# Função para carregar o arquivo JSON
def load_graph(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Main
def main():
    # Carrega o arquivo GRAFOS.json
    file_name = "GRAFOS.json"
    graphs = load_graph(file_name)

    # Pergunta ao usuário qual algoritmo aplicar
    print("Escolha o algoritmo para aplicar:")
    print("1. Ford-Fulkerson (Fluxo Máximo)")
    print("2. Sucessivos Caminhos Mínimos (Fluxo de Custo Mínimo)")

    choice = input("Digite 1 ou 2: ")

    source = input("Digite o nó de origem (ex: 's'): ")
    sink = input("Digite o nó de destino (ex: 't'): ")

    if choice == '1':
        # Executa o algoritmo de Ford-Fulkerson no grafo 1
        ff = FordFulkerson(graphs['graph_1'])
        max_flow = ff.ford_fulkerson(source, sink)
        print(f"O fluxo máximo é: {max_flow}")

    elif choice == '2':
        # Executa o algoritmo de Sucessivos Caminhos Mínimos no grafo 2
        sp = SuccessiveShortestPaths(graphs['graph_2'])
        max_flow, min_cost = sp.successive_shortest_paths(source, sink)
        print(f"O fluxo máximo é: {max_flow}")
        print(f"O custo mínimo é: {min_cost}")
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()