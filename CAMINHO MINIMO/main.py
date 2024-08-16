from Dijkstra import Dijkstra
from Bellman_Ford import BellmanFord
from Floyd_Warshall import FloydWarshall
from Grafo import Grafo

def exibir_menu():
    print("\nEscolha o algoritmo a ser executado:")
    print("1 - Dijkstra")
    print("2 - Bellman-Ford")
    print("3 - Floyd-Warshall")
    print("0 - Sair")

def main():
    grafo = Grafo()
    
    # Carrega o grafo a partir do arquivo JSON
    grafo.carregar_do_json('grafo.json')
    
    while True:
        exibir_menu()
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            dijkstra = Dijkstra(grafo)
            no_inicial = 0
            distancias = dijkstra.calcular_menor_caminho(no_inicial)
            print(f"Distâncias mínimas do nó {no_inicial} para os demais nós usando Dijkstra:")
            for no, distancia in distancias.items():
                print(f"Distância até o nó {no}: {distancia}")
        
        elif escolha == '2':
            bellman_ford = BellmanFord(grafo)
            no_inicial = 0
            try:
                distancias = bellman_ford.calcular_menor_caminho(no_inicial)
                print(f"Distâncias mínimas do nó {no_inicial} para os demais nós usando Bellman-Ford:")
                for no, distancia in distancias.items():
                    print(f"Distância até o nó {no}: {distancia}")
            except ValueError as e:
                print(e)
                
        elif escolha == '3':
            floyd_warshall = FloydWarshall(grafo)
            distancias = floyd_warshall.calcular_todos_caminhos_minimos()
            print("Matriz de distâncias mínimas usando Floyd-Warshall:")
            for origem, destinos in distancias.items():
                for destino, distancia in destinos.items():
                    distancia_legivel = distancia if distancia != float('infinity') else "Sem caminho"
                    print(f"Do nó {origem} até o nó {destino}: {distancia_legivel}")
        
        elif escolha == '0':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
