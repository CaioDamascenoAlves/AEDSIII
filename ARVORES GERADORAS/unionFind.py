class UnionFind:
    def __init__(self, n):
        """Inicializa a estrutura Union-Find para 'n' elementos."""
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        """Encontra o representante do conjunto de 'u'."""
        if u != self.pai[u]:
            self.pai[u] = self.find(self.pai[u])
        return self.pai[u]

    def union(self, u, v):
        """Une os conjuntos de 'u' e 'v'."""
        raiz_u = self.find(u)
        raiz_v = self.find(v)

        if raiz_u != raiz_v:
            # União por rank
            if self.rank[raiz_u] > self.rank[raiz_v]:
                self.pai[raiz_v] = raiz_u
            elif self.rank[raiz_u] < self.rank[raiz_v]:
                self.pai[raiz_u] = raiz_v
            else:
                self.pai[raiz_v] = raiz_u
                self.rank[raiz_u] += 1