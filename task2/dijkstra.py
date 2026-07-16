import heapq
from graph import Graph

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    previous = {node: None for node in graph.nodes()}
    visited = set()

    pq =[(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph.get_neighbors(u):
            if weight < 0:
                raise ValueError("Dijkstra's algorithm does not support negative edge weights")
            if v in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                previous[v] = u
                heapq.heappush(pq, (new_dist, v))

    return distances, previous

def get_path(previous, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path


if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 1)
    g.add_edge("C", "B", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)

    distances, previous = dijkstra(g, "A")

    print("Shortest distances from A:")
    for node, dist in distances.items():
        print(f"  A -> {node}: {dist}")

    print("\nShortest path from A to D:", get_path(previous, "D"))
