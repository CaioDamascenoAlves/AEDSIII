import csv
import json
from collections import defaultdict

class Disciplina:
    def __init__(self, codigo, nome, periodo, pre_requisitos):
        self.codigo = codigo
        self.nome = nome
        self.periodo = periodo
        self.pre_requisitos = pre_requisitos
        self.peso = 1
        self.inicio_mais_cedo = 0
        self.termino_mais_cedo = 0
        self.inicio_mais_tarde = float('inf')
        self.termino_mais_tarde = float('inf')
        self.folga_total = 0
        self.folga_livre = 0

def ler_arquivo(nome_arquivo):
    if nome_arquivo.endswith('.csv'):
        return ler_csv(nome_arquivo)
    elif nome_arquivo.endswith('.json'):
        return ler_json(nome_arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado. Use CSV ou JSON.")

def ler_csv(nome_arquivo):
    disciplinas = {}
    codificacoes = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    for codificacao in codificacoes:
        try:
            with open(nome_arquivo, 'r', encoding=codificacao) as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    codigo = linha['Código']
                    nome = linha['Nome']
                    periodo = int(linha['Período'])
                    pre_requisitos = linha['Dependências'].split(',') if linha['Dependências'] else []
                    disciplinas[codigo] = Disciplina(codigo, nome, periodo, pre_requisitos)
            return disciplinas
        except UnicodeDecodeError:
            continue
    raise ValueError("Não foi possível ler o arquivo CSV com nenhuma das codificações tentadas.")

def ler_json(nome_arquivo):
    # Tente diferentes codificações
    codificacoes = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    for codificacao in codificacoes:
        try:
            with open(nome_arquivo, 'r', encoding=codificacao) as arquivo:
                dados = json.load(arquivo)
            
            disciplinas = {}
            for disc in dados['disciplinas']:
                codigo = disc['codigo']
                nome = disc['nome']
                periodo = int(disc['periodo'])
                pre_requisitos = disc.get('pre_requisitos', [])  # Usa uma lista vazia se não houver pré-requisitos
                disciplinas[codigo] = Disciplina(codigo, nome, periodo, pre_requisitos)
            return disciplinas
        except UnicodeDecodeError:
            continue  # Tenta a próxima codificação
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON com codificação {codificacao}. Tentando próxima codificação.")
            continue
    
    # Se nenhuma codificação funcionou
    raise ValueError("Não foi possível ler o arquivo JSON com nenhuma das codificações tentadas.")

def calcular_caminho_critico(disciplinas):
    # Calcula o início e término mais cedo
    for disciplina in disciplinas.values():
        if not disciplina.pre_requisitos:
            disciplina.inicio_mais_cedo = 1
            disciplina.termino_mais_cedo = disciplina.inicio_mais_cedo + disciplina.peso - 1
        else:
            disciplina.inicio_mais_cedo = max(disciplinas[pre_req].termino_mais_cedo + 1 for pre_req in disciplina.pre_requisitos)
            disciplina.termino_mais_cedo = disciplina.inicio_mais_cedo + disciplina.peso - 1

    # Calcula o início e término mais tarde
    for disciplina in reversed(list(disciplinas.values())):
        sucessores = [d for d in disciplinas.values() if disciplina.codigo in d.pre_requisitos]
        if not sucessores:
            disciplina.termino_mais_tarde = max(d.termino_mais_cedo for d in disciplinas.values())
            disciplina.inicio_mais_tarde = disciplina.termino_mais_tarde - disciplina.peso + 1
        else:
            disciplina.termino_mais_tarde = min(sucessor.inicio_mais_tarde - 1 for sucessor in sucessores)
            disciplina.inicio_mais_tarde = disciplina.termino_mais_tarde - disciplina.peso + 1

    # Calcula as folgas
    for disciplina in disciplinas.values():
        disciplina.folga_total = disciplina.inicio_mais_tarde - disciplina.inicio_mais_cedo
        disciplina.folga_livre = min((sucessor.inicio_mais_cedo - disciplina.termino_mais_cedo - 1) 
                                     for sucessor in disciplinas.values() if disciplina.codigo in sucessor.pre_requisitos) if [d for d in disciplinas.values() if disciplina.codigo in d.pre_requisitos] else 0

def identificar_caminho_critico(disciplinas):
    return [disc for disc in disciplinas.values() if disc.folga_total == 0]

def imprimir_resultados(disciplinas, caminho_critico):
    print("Resultados do cálculo do caminho crítico:")
    for disciplina in disciplinas.values():
        print(f"{disciplina.codigo} - {disciplina.nome}:")
        print(f"  Início Mais Cedo: {disciplina.inicio_mais_cedo}")
        print(f"  Término Mais Cedo: {disciplina.termino_mais_cedo}")
        print(f"  Início Mais Tarde: {disciplina.inicio_mais_tarde}")
        print(f"  Término Mais Tarde: {disciplina.termino_mais_tarde}")
        print(f"  Folga Total: {disciplina.folga_total}")
        print(f"  Folga Livre: {disciplina.folga_livre}")
        print()

    print("Caminho Crítico:")
    for disciplina in caminho_critico:
        print(f"{disciplina.codigo} - {disciplina.nome}")

def main():
    nome_arquivo = input("Digite o nome do arquivo (CSV ou JSON): ")
    disciplinas = ler_arquivo(nome_arquivo)
    calcular_caminho_critico(disciplinas)
    caminho_critico = identificar_caminho_critico(disciplinas)
    imprimir_resultados(disciplinas, caminho_critico)

if __name__ == "__main__":
    main()