import heapq
from graph import Graph

def prim(graph, start):
    visited = set([start])
    mst_edges = []
    total_weight = 0

    edges = [(w, start, v) for v, w in graph.get_neighbors(start)]
    heapq.heapify(edges)

    while edges and len(visited) < graph.num_nodes():
        weight, u, v = heapq.heappop(edges)

        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight

        for next_v, next_w in graph.get_neighbors(v):
            if next_v not in visited:
                heapq.heappush(edges, (next_w, v, next_v))

    return mst_edges, total_weight


if __name__ == "__main__":
    g = Graph(directed=False)
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 1)
    g.add_edge("C", "B", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)

    mst_edges, total_weight = prim(g, "A")

    print("Minimum Spanning Tree edges:")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} (weight {w})")

    print(f"\nTotal MST weight: {total_weight}")