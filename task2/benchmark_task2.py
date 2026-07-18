import time
import random
import matplotlib.pyplot as plt
from graph import Graph
from dijkstra import dijkstra
from prim import prim
from bellman_ford import bellman_ford


def generate_random_graph(num_nodes, num_edges, directed=True, allow_negative=False):
    g = Graph(directed=directed)
    nodes = [f"N{i}" for i in range(num_nodes)]
    for node in nodes:
        g.add_node(node)

    edges_added = 0
    attempts = 0
    while edges_added < num_edges and attempts < num_edges * 10:
        u, v = random.sample(nodes, 2)
        weight = random.randint(-5, 20) if allow_negative else random.randint(1, 20)
        g.add_edge(u, v, weight)
        edges_added += 1
        attempts += 1

    return g, nodes


def benchmark(sizes, runs=3):
    results = {"Dijkstra": [], "Prim": [], "BellmanFord": []}

    for n in sizes:
        num_edges = n * 3  
        dij_times, prim_times, bf_times = [], [], []

        for _ in range(runs):
            # Directed graph, non-negative weights (for Dijkstra + Bellman-Ford)
            g_directed, nodes = generate_random_graph(n, num_edges, directed=True, allow_negative=False)
            source = nodes[0]

            t0 = time.perf_counter()
            dijkstra(g_directed, source)
            dij_times.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            bellman_ford(g_directed, source)
            bf_times.append(time.perf_counter() - t0)

            # Undirected graph (for Prim's MST)
            g_undirected, nodes_u = generate_random_graph(n, num_edges, directed=False, allow_negative=False)

            t0 = time.perf_counter()
            prim(g_undirected, nodes_u[0])
            prim_times.append(time.perf_counter() - t0)

        avg_dij = sum(dij_times) / runs
        avg_prim = sum(prim_times) / runs
        avg_bf = sum(bf_times) / runs

        results["Dijkstra"].append(avg_dij)
        results["Prim"].append(avg_prim)
        results["BellmanFord"].append(avg_bf)

        print(f"n={n:<6} Dijkstra={avg_dij:.5f}s  Prim={avg_prim:.5f}s  BellmanFord={avg_bf:.5f}s")

    return results


def plot_results(sizes, results):
    plt.figure()
    for algo, times in results.items():
        plt.plot(sizes, times, marker='o', label=algo)
    plt.xlabel("Number of nodes (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Algorithm runtime vs graph size")
    plt.legend()
    plt.grid(True)
    plt.savefig("task2_comparison.png")
    plt.close()
    print("Saved task2_comparison.png")


if __name__ == "__main__":
    sizes = [50, 200, 500]
    results = benchmark(sizes)
    plot_results(sizes, results)