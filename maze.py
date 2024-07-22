class Maze:
    def __init__(self, arquivo):
        self.labirinto = self.ler_labirinto(arquivo)

    def ler_labirinto(self, arquivo):
        with open(arquivo, 'r') as f:
            labirinto = [list(linha.strip()) for linha in f]
        return labirinto

    def encontrar_ponto(self, ponto):
        for i, linha in enumerate(self.labirinto):
            for j, celula in enumerate(linha):
                if celula == ponto:
                    return i, j
        return None

    def get_labirinto(self):
        return self.labirinto
