import time
import random
from bst import BST
from avl import AVLTree
from min_heap import MinHeap
from hash_table import HashTable


def generate_cities(n):
    return [(random.uniform(0, 100000), f"City{i}") for i in range(n)]


def benchmark(n, runs=5):
    results = {"BST": {}, "AVL": {}, "HashTable": {}}

    for _ in range(runs):
        cities = generate_cities(n)
        search_keys = random.sample([c[0] for c in cities], min(1000, n))

        bst = BST()
        t0 = time.perf_counter()
        for k, name in cities:
            bst.insert(k, name)
        t_insert = time.perf_counter() - t0

        t0 = time.perf_counter()
        for k in search_keys:
            bst.search(k)
        t_search = time.perf_counter() - t0

        t0 = time.perf_counter()
        for k in search_keys:
            bst.delete(k)
        t_delete = time.perf_counter() - t0

        for label, val in [("insert", t_insert), ("search", t_search), ("delete", t_delete)]:
            results["BST"].setdefault(label, []).append(val)

        avl = AVLTree()
        t0 = time.perf_counter()
        for k, name in cities:
            avl.insert(k, name)
        t_insert = time.perf_counter() - t0

        t0 = time.perf_counter()
        for k in search_keys:
            avl.search(k)
        t_search = time.perf_counter() - t0

        t0 = time.perf_counter()
        for k in search_keys:
            avl.delete(k)
        t_delete = time.perf_counter() - t0

        for label, val in [("insert", t_insert), ("search", t_search), ("delete", t_delete)]:
            results["AVL"].setdefault(label, []).append(val)

        ht = HashTable(size=max(1024, n * 2))
        t0 = time.perf_counter()
        for k, name in cities:
            ht.insert(name, k)
        t_insert = time.perf_counter() - t0

        search_names = [c[1] for c in cities][:len(search_keys)]
        t0 = time.perf_counter()
        for name in search_names:
            ht.search(name)
        t_search = time.perf_counter() - t0

        t0 = time.perf_counter()
        for name in search_names:
            ht.delete(name)
        t_delete = time.perf_counter() - t0

        for label, val in [("insert", t_insert), ("search", t_search), ("delete", t_delete)]:
            results["HashTable"].setdefault(label, []).append(val)

    print(f"\n--- n = {n} (avg over {runs} runs, seconds) ---")
    print(f"{'Structure':<12}{'Insert':<12}{'Search':<12}{'Delete':<12}")
    for struct, ops in results.items():
        row = f"{struct:<12}"
        for op in ["insert", "search", "delete"]:
            avg = sum(ops[op]) / len(ops[op])
            row += f"{avg:<12.5f}"
        print(row)

    return results


def benchmark_heap(n):
    cities = generate_cities(n)
    heap = MinHeap()

    t0 = time.perf_counter()
    for k, name in cities:
        heap.insert(k, name)
    t_insert = time.perf_counter() - t0

    t0 = time.perf_counter()
    while not heap.is_empty():
        heap.extract_min()
    t_extract = time.perf_counter() - t0

    print(f"n={n:<6} insert={t_insert:.5f}s  extract_all={t_extract:.5f}s")
    return t_insert, t_extract


if __name__ == "__main__":
    ns = [100, 1000, 10000]
    all_results = {}

    for n in ns:
        all_results[n] = benchmark(n)

    print("\n--- Min-Heap insert + extract-all timing ---")
    for n in ns:
        benchmark_heap(n)