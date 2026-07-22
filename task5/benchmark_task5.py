import time
import matplotlib.pyplot as plt
from bfs_sequential import bfs_sequential, generate_large_graph
from bfs_concurrent import bfs_concurrent


def run_speedup_analysis(num_nodes=1000, avg_degree=4, thread_counts=(1, 2, 4, 8), trials=3):
    g, nodes = generate_large_graph(num_nodes=num_nodes, avg_degree=avg_degree)
    start = nodes[0]

    # Sequential baseline
    seq_times = []
    for _ in range(trials):
        t0 = time.perf_counter()
        bfs_sequential(g, start)
        seq_times.append(time.perf_counter() - t0)
    avg_seq_time = sum(seq_times) / trials
    print(f"Sequential BFS baseline: {avg_seq_time:.5f}s (avg of {trials} runs)")

    # Concurrent, at each thread count
    results = {}
    for num_threads in thread_counts:
        times = []
        for _ in range(trials):
            t0 = time.perf_counter()
            bfs_concurrent(g, start, num_threads=num_threads)
            times.append(time.perf_counter() - t0)
        avg_time = sum(times) / trials
        speedup = avg_seq_time / avg_time if avg_time > 0 else 0
        results[num_threads] = {"time": avg_time, "speedup": speedup}
        print(f"Threads={num_threads:<2} avg_time={avg_time:.5f}s  speedup={speedup:.2f}x")

    return avg_seq_time, results


def plot_speedup(thread_counts, results):
    speedups = [results[t]["speedup"] for t in thread_counts]
    ideal = list(thread_counts)  # ideal linear speedup line for reference

    plt.figure()
    plt.plot(thread_counts, speedups, marker='o', label="Observed speedup")
    plt.plot(thread_counts, ideal, linestyle='--', label="Ideal linear speedup")
    plt.xlabel("Number of threads")
    plt.ylabel("Speedup (relative to sequential)")
    plt.title("BFS Speedup vs Thread Count")
    plt.legend()
    plt.grid(True)
    plt.savefig("task5_speedup.png")
    plt.close()
    print("Saved task5_speedup.png")


if __name__ == "__main__":
    thread_counts = (1, 2, 4, 8)
    avg_seq_time, results = run_speedup_analysis(
        num_nodes=1000, avg_degree=4, thread_counts=thread_counts, trials=3
    )
    plot_speedup(thread_counts, results)