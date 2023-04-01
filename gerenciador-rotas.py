# Importando o pacote deque para implementar a lista de nós adjacentes
from collections import deque

# Classe para representar o grafo
class Grafo:
    def __init__(self, arestas):
        self.adj = {}
        # Criando a lista de adjacências
        for u, v, w in arestas:
            if u not in self.adj:
                self.adj[u] = []
            self.adj[u].append((v, w))
            if v not in self.adj:
                self.adj[v] = []
            self.adj[v].append((u, w))

    def busca_caminho(self, origem, destino):
        # Inicializando a fila de nós a serem visitados
        fila = deque()
        fila.append(origem)
        # Inicializando o dicionário de distâncias
        dist = {origem: 0}
        # Inicializando o dicionário de predecessores
        pred = {origem: None}

        # Executando a busca em largura
        while fila:
            u = fila.popleft()
            if u == destino:
                # Se chegamos ao destino, interrompemos a busca
                break
            for v, w in self.adj[u]:
                if v not in dist:
                    # Se o nó ainda não foi visitado, adicionamos na fila
                    fila.append(v)
                    # Atualizando a distância e o predecessor
                    dist[v] = dist[u] + w
                    pred[v] = u

        # Montando o caminho percorrido
        caminho = [destino]
        while pred[caminho[-1]] is not None:
            caminho.append(pred[caminho[-1]])
        caminho.reverse()

        # Retornando o caminho e a distância total
        return caminho, dist[destino]

# Criando o objeto Grafo com as informações da rede de computadores
grafo = Grafo([
    ('A', 'B', 2),
    ('A', 'C', 1),
    ('B', 'D', 3),
    ('B', 'E', 2),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'F', 2),
    ('E', 'F', 3)
])

# Chamando o método busca_caminho para encontrar a rota mais curta entre A e F
caminho, dist = grafo.busca_caminho('A', 'F')

# Imprimindo o resultado
print(f'Rota: {" -> ".join(caminho)}')
print(f'Distância total: {dist}')
