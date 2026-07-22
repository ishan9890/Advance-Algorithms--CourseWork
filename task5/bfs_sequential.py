import time
from collections import deque
from graph import Graph


def bfs_sequential(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor, weight in graph.get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def generate_large_graph(num_nodes, avg_degree=4):
    import random
    g = Graph(directed=False)
    nodes = [f"N{i}" for i in range(num_nodes)]
    for node in nodes:
        g.add_node(node)

    num_edges = num_nodes * avg_degree
    for _ in range(num_edges):
        u, v = random.sample(nodes, 2)
        g.add_edge(u, v, 1)  

    return g, nodes


if __name__ == "__main__":
    g, nodes = generate_large_graph(num_nodes=1000, avg_degree=4)

    t0 = time.perf_counter()
    order = bfs_sequential(g, nodes[0])
    elapsed = time.perf_counter() - t0

    print(f"Sequential BFS visited {len(order)} nodes out of {len(nodes)} total")
    print(f"First 10 nodes visited: {order[:10]}")
    print(f"Time taken: {elapsed:.5f}s")