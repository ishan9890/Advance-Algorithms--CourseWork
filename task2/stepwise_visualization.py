import heapq
from graph import Graph


def dijkstra_stepwise(graph, source):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    previous = {node: None for node in graph.nodes()}
    visited = set()
    pq = [(0, source)]
    step = 0

    print(f"--- Dijkstra step-by-step from source '{source}' ---")
    while pq:
        current_dist, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        step += 1

        print(f"\nStep {step}: visiting node '{u}' (distance = {current_dist})")
        for v, weight in graph.get_neighbors(u):
            if v in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < distances[v]:
                old = distances[v]
                distances[v] = new_dist
                previous[v] = u
                heapq.heappush(pq, (new_dist, v))
                print(f"   relax edge {u}->{v} (weight {weight}): "
                      f"distance[{v}] updated {old} -> {new_dist}")

        print(f"   Current distances: {distances}")
        print(f"   Visited so far: {visited}")

    return distances, previous


def prim_stepwise(graph, start):
    visited = set([start])
    mst_edges = []
    total_weight = 0
    step = 0

    edges = [(w, start, v) for v, w in graph.get_neighbors(start)]
    heapq.heapify(edges)

    print(f"\n--- Prim step-by-step from start '{start}' ---")
    while edges and len(visited) < graph.num_nodes():
        weight, u, v = heapq.heappop(edges)
        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight
        step += 1

        print(f"\nStep {step}: add edge {u}--{v} (weight {weight})")
        print(f"   MST so far: {mst_edges}")
        print(f"   Total weight so far: {total_weight}")
        print(f"   Visited nodes: {visited}")

        for next_v, next_w in graph.get_neighbors(v):
            if next_v not in visited:
                heapq.heappush(edges, (next_w, v, next_v))

    return mst_edges, total_weight


if __name__ == "__main__":
    # Small demo graph, same one used in earlier Task 2 tests
    g_directed = Graph(directed=True)
    g_directed.add_edge("A", "B", 4)
    g_directed.add_edge("A", "C", 1)
    g_directed.add_edge("C", "B", 2)
    g_directed.add_edge("B", "D", 5)
    g_directed.add_edge("C", "D", 8)

    dijkstra_stepwise(g_directed, "A")

    g_undirected = Graph(directed=False)
    g_undirected.add_edge("A", "B", 4)
    g_undirected.add_edge("A", "C", 1)
    g_undirected.add_edge("C", "B", 2)
    g_undirected.add_edge("B", "D", 5)
    g_undirected.add_edge("C", "D", 8)

    prim_stepwise(g_undirected, "A")