import random

class Item:
    def __init__(self, item_id, demands):
        """demands: list of resource requirements, e.g. [cpu, ram, bandwidth]"""
        self.id = item_id
        self.demands = demands

    def total_weight(self):
        return sum(self.demands)

    def __repr__(self):
        return f"Item{self.id}{self.demands}"


class Bin:
    def __init__(self, capacity):
        """capacity: list of max capacity per dimension, e.g. [10, 10, 10]"""
        self.capacity = capacity
        self.items = []
        self.used = [0] * len(capacity)

    def can_fit(self, item):
        return all(self.used[d] + item.demands[d] <= self.capacity[d]
                   for d in range(len(self.capacity)))

    def add_item(self, item):
        self.items.append(item)
        for d in range(len(self.capacity)):
            self.used[d] += item.demands[d]

    def remove_item(self, item):
        self.items.remove(item)
        for d in range(len(self.capacity)):
            self.used[d] -= item.demands[d]

    def __repr__(self):
        return f"Bin(used={self.used}, items={self.items})"


def generate_random_items(n, num_dimensions=3, max_demand=10, seed=None):
    if seed is not None:
        random.seed(seed)
    return [Item(i, [random.randint(1, max_demand) for _ in range(num_dimensions)])
             for i in range(n)]


def first_fit_decreasing(items, capacity):
    """Greedy construction heuristic: sort items by total weight (desc),
    place each into the first bin that fits, else open a new bin."""
    sorted_items = sorted(items, key=lambda it: it.total_weight(), reverse=True)
    bins = []

    for item in sorted_items:
        placed = False
        for b in bins:
            if b.can_fit(item):
                b.add_item(item)
                placed = True
                break
        if not placed:
            new_bin = Bin(capacity[:])
            new_bin.add_item(item)
            bins.append(new_bin)

    return bins


def print_solution(bins, label=""):
    print(f"\n{label} solution: {len(bins)} bins used")
    for i, b in enumerate(bins):
        print(f"  Bin {i}: used={b.used}, capacity={b.capacity}, items={[it.id for it in b.items]}")


if __name__ == "__main__":
    capacity = [15, 15, 15] 
    items = generate_random_items(n=20, num_dimensions=3, max_demand=10, seed=42)

    print("Items generated:")
    for it in items:
        print(f"  {it}")

    bins = first_fit_decreasing(items, capacity)
    print_solution(bins, "Greedy (First-Fit Decreasing)")