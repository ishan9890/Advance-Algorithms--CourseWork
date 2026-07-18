from graph import Graph

def bellman_ford(graph, source):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    previous = {node: None for node in graph.nodes()}

    edges = graph.get_all_edges()
    n = graph.num_nodes()

    for i in range(n - 1):
        updated = False
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                previous[v] = u
                updated = True
        if not updated:
            break  

    has_negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break

    return distances, previous, has_negative_cycle


if __name__ == "__main__":
    # Test 1: graph with a negative edge but no negative cycle
    g1 = Graph(directed=True)
    g1.add_edge("A", "B", 4)
    g1.add_edge("A", "C", 1)
    g1.add_edge("C", "B", -2)
    g1.add_edge("B", "D", 5)
    g1.add_edge("C", "D", 8)

    distances, previous, has_cycle = bellman_ford(g1, "A")
    print("Test 1 - Graph with negative edge (no cycle):")
    for node, dist in distances.items():
        print(f"  A -> {node}: {dist}")
    print("Negative cycle detected:", has_cycle)

    # Test 2: graph WITH a negative cycle
    g2 = Graph(directed=True)
    g2.add_edge("A", "B", 1)
    g2.add_edge("B", "C", -1)
    g2.add_edge("C", "A", -1)

    distances2, previous2, has_cycle2 = bellman_ford(g2, "A")
    print("\nTest 2 - Graph WITH negative cycle:")
    print("Negative cycle detected:", has_cycle2)