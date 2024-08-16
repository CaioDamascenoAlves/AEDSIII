import json

class Grafo:
    def __init__(self):
        self.arestas = {}
    
    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.arestas:
            self.arestas[origem] = []
        self.arestas[origem].append((destino, peso))

    def carregar_do_json(self, arquivo_json):
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
            for aresta in dados['edges']:
                self.adicionar_aresta(aresta['source'], aresta['target'], aresta['weight'])
