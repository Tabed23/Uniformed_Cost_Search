from graph import Graph

graph = {
    'S': ['A', 'D', 'C'],
    'D': ['B', 'G'],
    'C': ['F'],
    'B': ['E'],
    'F': ['E'],
    'E': ['G'],
    'A': [],
}
if __name__ == '__main__':
    g = Graph()
    g.set_graph(graph)
    print(g.get_graph())
    print("Visited node :", g.Uniformed_cost_search('S',  'G'))