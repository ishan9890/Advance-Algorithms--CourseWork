import time
import threading
import queue
from graph import Graph
from bfs_sequential import generate_large_graph


def bfs_concurrent(graph, start, num_threads=4):
    visited = set([start])
    visited_lock = threading.Lock()   

    work_queue = queue.Queue()        
    work_queue.put(start)

    order = []
    order_lock = threading.Lock()     

    active_tasks = [1]                
    active_lock = threading.Lock()

    def worker():
        while True:
            try:
                node = work_queue.get(timeout=0.5)
            except queue.Empty:
                return  # no more work available, thread can exit

            with order_lock:
                order.append(node)

            neighbors = graph.get_neighbors(node)
            new_nodes = []
            with visited_lock:
                for neighbor, weight in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        new_nodes.append(neighbor)

            with active_lock:
                active_tasks[0] += len(new_nodes)
                active_tasks[0] -= 1

            for n in new_nodes:
                work_queue.put(n)

            work_queue.task_done()

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return order


if __name__ == "__main__":
    g, nodes = generate_large_graph(num_nodes=1000, avg_degree=4)

    for num_threads in [1, 2, 4, 8]:
        t0 = time.perf_counter()
        order = bfs_concurrent(g, nodes[0], num_threads=num_threads)
        elapsed = time.perf_counter() - t0
        print(f"Threads={num_threads:<2} visited={len(order):<5} time={elapsed:.5f}s")