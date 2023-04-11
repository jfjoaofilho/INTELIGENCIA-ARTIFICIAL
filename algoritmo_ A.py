
#importando a biblioteca que contém a classe PriorityQueue
from queue import PriorityQueue

# definindo a classe A*
class AStar:
    # inicializando o algoritmo
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.frontier = PriorityQueue()
        self.frontier.put((0, start))
        self.visited = set()
        self.cost_so_far = {}
        self.cost_so_far[start] = 0
        self.came_from = {}
        self.came_from[start] = None
    
    # buscando a solução
    def search(self):
        while not self.frontier.empty():
            current_cost, current_node = self.frontier.get()
            if current_node == self.goal:
                break
            for neighboor in self.graph[current_node]:
                cost = self.graph[current_node][neighboor]
                new_cost = current_cost + cost
                if neighboor not in self.visited or new_cost < self.cost_so_far[neighboor]:
                    self.cost_so_far[neighboor] = new_cost
                    priority = new_cost + self.heuristic(neighboor, self.goal)
                    self.frontier.put((priority, neighboor))
                    self.came_from[neighboor] = current_node
            self.visited.add(current_node)
        return self.came_from
    
    # heuristica da busca
    def heuristic(self, node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# definindo o grafo
graph = {
        (0, 0): {(0, 1): 1, (1, 0): 1, (1, 1): 2},
        (0, 1): {(0, 0): 1, (1, 1): 3, (1, 0): 1},
        (1, 0): {(0, 0): 1, (1, 1): 2, (0, 1): 1},
        (1, 1): {(1, 0): 2, (0, 1): 3, (0, 0): 2}
        }

# definindo o início e o fim
start = (0, 0)
goal = (1, 1)

# implementando o algoritmo
astar = AStar(graph, start, goal)
came_from = astar.search()

# imprimindo o resultado
print(came_from)
