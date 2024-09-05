# Importação das bibliotecas necessárias
import csv
from collections import defaultdict

class AnalisadorCaminhoCritico:
    def __init__(self, nome_arquivo):
        # Inicializa a classe com o nome do arquivo a ser analisado
        self.nome_arquivo = nome_arquivo
        # Cria um dicionário padrão para armazenar o grafo
        self.grafo = defaultdict(list)
        # Cria um dicionário para armazenar as informações das tarefas
        self.tarefas = {}

    def ler_csv(self):
        # Abre o arquivo CSV para leitura
        with open(self.nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Cria um leitor CSV que interpreta a primeira linha como cabeçalho
            leitor_csv = csv.DictReader(arquivo)
            # Itera sobre cada linha do arquivo CSV
            for linha in leitor_csv:
                # Extrai o código da tarefa
                codigo = linha['Código']
                # Armazena as informações da tarefa no dicionário de tarefas
                self.tarefas[codigo] = {
                    'nome': linha['Nome'],
                    'periodo': int(linha['Período']),
                    'duracao': int(linha['Duração'])
                }
                # Processa as dependências da tarefa
                dependencias = linha['Dependências'].split(';') if linha['Dependências'] else []
                # Adiciona as dependências ao grafo
                for dep in dependencias:
                    if dep:
                        self.grafo[dep].append(codigo)

    def bellman_ford_caminho_mais_longo(self):
        # Inicializa o dicionário de distâncias com -infinito para todas as tarefas
        distancia = {tarefa: float('-inf') for tarefa in self.tarefas}
        # Define a distância do nó de início como 0
        distancia['INICIO'] = 0
        # Define a distância do nó de fim como -infinito inicialmente
        distancia['FIM'] = float('-inf')
        
        # Inicializa o dicionário de predecessores
        predecessor = {tarefa: None for tarefa in self.tarefas}
        predecessor['INICIO'] = None
        predecessor['FIM'] = None
        
        # Adiciona nós de início e fim ao grafo
        for tarefa in self.tarefas:
            # Se a tarefa não tem dependências, conecta-a ao nó de início
            if not any(tarefa in deps for deps in self.grafo.values()):
                self.grafo['INICIO'].append(tarefa)
            # Se a tarefa não tem sucessores, conecta-a ao nó de fim
            if tarefa not in self.grafo:
                self.grafo[tarefa].append('FIM')
        
        # Relaxa as arestas |V| - 1 vezes, onde |V| é o número de vértices
        for _ in range(len(self.tarefas) + 2):  # +2 para incluir INICIO e FIM
            for u in self.grafo:
                for v in self.grafo[u]:
                    # Define o peso da aresta
                    peso = self.tarefas[v]['duracao'] if v != 'FIM' else 0
                    # Relaxa a aresta se um caminho mais longo for encontrado
                    if distancia[u] + peso > distancia[v]:
                        distancia[v] = distancia[u] + peso
                        predecessor[v] = u

        # Verifica se há ciclos de peso positivo
        for u in self.grafo:
            for v in self.grafo[u]:
                peso = self.tarefas[v]['duracao'] if v != 'FIM' else 0
                if distancia[u] + peso > distancia[v]:
                    raise ValueError("O grafo contém um ciclo de peso positivo")

        return distancia, predecessor

    def obter_caminho_critico(self, predecessor, fim):
        # Inicializa uma lista vazia para armazenar o caminho
        caminho = []
        # Começa do nó final e retrocede até o nó inicial
        atual = fim
        while atual != 'INICIO':
            caminho.append(atual)
            atual = predecessor[atual]
        # Inverte o caminho para obter a ordem correta
        caminho.reverse()
        # Remove o nó 'FIM' do caminho
        return caminho[:-1]

    def analisar(self):
        # Lê o arquivo CSV e constrói o grafo
        self.ler_csv()
        
        try:
            # Executa o algoritmo de Bellman-Ford modificado
            distancia, predecessor = self.bellman_ford_caminho_mais_longo()
            # Obtém o caminho crítico
            caminho_critico = self.obter_caminho_critico(predecessor, 'FIM')
            
            # Imprime o caminho crítico
            print("Caminho crítico:")
            for tarefa in caminho_critico:
                if tarefa in self.tarefas:
                    print(f"{tarefa}: {self.tarefas[tarefa]['nome']}")
            
            # Imprime o tempo mínimo de conclusão
            print(f"\nTempo mínimo de conclusão: {distancia['FIM']} períodos")
        
        except ValueError as e:
            # Captura e imprime qualquer erro encontrado
            print(f"Erro: {e}")