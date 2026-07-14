import matplotlib.pyplot as plt
from benchmark_task1 import benchmark, benchmark_heap

def collect_results(ns):
    all_results = {}
    for n in ns:
        all_results[n] = benchmark(n)
    return all_results

def plot_operation(all_results, ns, operation):
    plt.figure()
    for struct in ["BST", "AVL", "HashTable"]:
        times = [
            sum(all_results[n][struct][operation]) / len(all_results[n][struct][operation])
            for n in ns
        ]
        plt.plot(ns, times, marker='o', label=struct)

    plt.xlabel("Number of cities (n)")
    plt.ylabel("Time (seconds)")
    plt.title(f"{operation.capitalize()} time vs n")
    plt.legend()
    plt.grid(True)
    filename = f"{operation}_comparison.png"
    plt.savefig(filename)
    plt.close()
    print(f"Saved {filename}")

def plot_heap(ns):
    inserts, extracts = [], []
    for n in ns:
        t_insert, t_extract = benchmark_heap(n)
        inserts.append(t_insert)
        extracts.append(t_extract)

    plt.figure()
    plt.plot(ns, inserts, marker='o', label="Insert")
    plt.plot(ns, extracts, marker='o', label="Extract-all")
    plt.xlabel("Number of cities (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Min-Heap: Insert vs Extract-all time")
    plt.legend()
    plt.grid(True)
    plt.savefig("heap_comparison.png")
    plt.close()
    print("Saved heap_comparison.png")


if __name__ == "__main__":
    ns = [100, 1000, 10000]
    all_results = collect_results(ns)

    plot_operation(all_results, ns, "insert")
    plot_operation(all_results, ns, "search")
    plot_operation(all_results, ns, "delete")
    plot_heap(ns)