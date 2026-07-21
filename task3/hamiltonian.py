class HamiltonianSolver:
    def __init__(self, graph):
        """graph: adjacency list dict, e.g. {0: [1, 2], 1: [0, 2], ...}"""
        self.graph = graph
        self.n = len(graph)
        self.nodes = list(graph.keys())

    def _is_valid(self, vertex, path, pos):
        # Pruning check 1: vertex must be adjacent to the previously placed vertex
        if vertex not in self.graph[path[pos - 1]]:
            return False
        # Pruning check 2: vertex must not already be in the path
        if vertex in path:
            return False
        return True

    def find_hamiltonian_path(self):
        for start in self.nodes:
            path = [start]
            if self._solve_path(path):
                return path
        return None

    def _solve_path(self, path):
        if len(path) == self.n:
            return True  # all vertices visited - path found

        for vertex in self.nodes:
            if self._is_valid(vertex, path, len(path)):
                path.append(vertex)
                if self._solve_path(path):
                    return True
                path.pop()  # backtrack: undo the choice and try another vertex

        return False

    def find_hamiltonian_cycle(self):
        start = self.nodes[0]
        path = [start]
        if self._solve_cycle(path):
            return path
        return None

    def _solve_cycle(self, path):
        if len(path) == self.n:
            # all vertices visited - check it can close back to start
            if path[0] in self.graph[path[-1]]:
                return True
            return False

        for vertex in self.nodes:
            if self._is_valid(vertex, path, len(path)):
                path.append(vertex)
                if self._solve_cycle(path):
                    return True
                path.pop()  # backtrack

        return False


if __name__ == "__main__":
    # Graph WITH a Hamiltonian cycle
    graph_with_cycle = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }

    solver1 = HamiltonianSolver(graph_with_cycle)
    path = solver1.find_hamiltonian_path()
    cycle = solver1.find_hamiltonian_cycle()
    print("Graph 1 (has cycle):")
    print("  Hamiltonian path:", path)
    print("  Hamiltonian cycle:", cycle)

    # Graph WITHOUT any Hamiltonian path 
    graph_no_path = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }

    solver2 = HamiltonianSolver(graph_no_path)
    path2 = solver2.find_hamiltonian_path()
    print("\nGraph 2 (no path possible):")
    print("  Hamiltonian path:", path2)