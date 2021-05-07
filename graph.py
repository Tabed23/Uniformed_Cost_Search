from queue import PriorityQueue


class Vertex:

    def __init__(self):
        self.edges = {}
        self.weights = {}

    def get_nighbors(self):
        return self.edges

    def get_cost(self, start_node, end_node):
        return self.weights[(start_node + end_node)]


class Graph:
    def __init__(self):
        self.__graph = {}
        self.__visited = []
        self.__frontier = PriorityQueue()
        self.vertex = Vertex()

    def set_graph(self, g):
        self.__graph = g

    def get_graph(self):
        return self.__graph

    def __push_node(self, cost, node):
        self.__frontier.put((cost, node))

    def __pop_node(self):
        return self.__frontier.get()

    @staticmethod
    def __get_cost(node_start, node_end, weight=None):
        return weight.get((node_start, node_end), 10000) if weight else 1

    def Uniformed_cost_search(self, start_node, goal_node, node_weight=None):
        self.__push_node(0, start_node)
        while self.__frontier:
            cost, node = self.__pop_node()
            if node not in self.__visited:
                self.__visited.append(node)
            if node == goal_node:
                print("goal found")
                break
            for neighbours in self.__graph[node]:
                if neighbours not in self.__visited:
                    self.__push_node(
                        cost + self.__get_cost(node, neighbours, node_weight),
                        neighbours)
        return self.__visited
