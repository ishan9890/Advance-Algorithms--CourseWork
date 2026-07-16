class Graph:
    def __init__(self, directed = True):
        self.directed = directed
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))
        
    def get_neighbors(self, node):
        return self.adj.get(node, [])
    
    def get_all_edges(self):
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                if not self.directed and (v, u) in seen:
                    continue
                edges.append((u,v,w))
                seen.add((u,v))
            return edges
        
    def num_nodes(self):
        return len(self.adj)
    def num_edges(self):
        return sum(len(neighbors) for neighbors in self.adj.values())
    def nodes(self):
        return list(self.adj.keys())
    
if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 1)
    g.add_edge("C", "B", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)

    print("Nodes:", g.nodes())
    print("Number of nodes:", g.num_nodes())
    print("Number of edges:", g.num_edges())
    print("Neighbors of A:", g.get_neighbors("A"))
    print("All edges:", g.get_all_edges())