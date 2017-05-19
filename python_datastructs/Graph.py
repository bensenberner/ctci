from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def add_undirected_edge(self, from_node, to_node, distance):
        self.add_edge(self, from_node, to_node, distance)
        self.add_edge(self, to_node, from_node, distance)

class Node:
    def __init__(self, name):
        self.name = name


