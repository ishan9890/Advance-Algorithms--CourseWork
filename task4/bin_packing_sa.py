import random
import math
import copy
from bin_packing_greedy import Item, Bin, generate_random_items, first_fit_decreasing, print_solution


def solution_cost(bins):
    """Objective: minimize number of bins used.
    Small tie-breaker penalty for imbalance encourages better-packed bins."""
    num_bins = len(bins)
    imbalance_penalty = 0
    for b in bins:
        for d in range(len(b.capacity)):
            free_space = b.capacity[d] - b.used[d]
            imbalance_penalty += free_space
    return num_bins * 1000 + imbalance_penalty  


def copy_solution(bins):
    return copy.deepcopy(bins)


def random_move(bins, capacity):
    """Try moving one random item from one bin to another (existing or new)."""
    bins = copy_solution(bins)
    non_empty_bins = [b for b in bins if b.items]
    if not non_empty_bins:
        return bins

    source_bin = random.choice(non_empty_bins)
    item = random.choice(source_bin.items)

    # candidate destinations: other existing bins + a brand new bin
    candidates = [b for b in bins if b is not source_bin]

    random.shuffle(candidates)
    for dest_bin in candidates:
        if dest_bin.can_fit(item):
            source_bin.remove_item(item)
            dest_bin.add_item(item)
            break
    else:
        if len(source_bin.items) > 1:
            source_bin.remove_item(item)
            new_bin = Bin(capacity[:])
            new_bin.add_item(item)
            bins.append(new_bin)

    # remove any bins left empty after the move
    bins = [b for b in bins if b.items]
    return bins


def simulated_annealing(initial_bins, capacity, initial_temp=100.0, cooling_rate=0.95, iterations_per_temp=50, min_temp=0.1):
    current = copy_solution(initial_bins)
    current_cost = solution_cost(current)
    best = copy_solution(current)
    best_cost = current_cost

    temp = initial_temp

    while temp > min_temp:
        for _ in range(iterations_per_temp):
            candidate = random_move(current, capacity)
            candidate_cost = solution_cost(candidate)
            delta = candidate_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / temp):
                current = candidate
                current_cost = candidate_cost

                if current_cost < best_cost:
                    best = copy_solution(current)
                    best_cost = current_cost

        temp *= cooling_rate

    return best, best_cost


if __name__ == "__main__":
    capacity = [15, 15, 15]
    items = generate_random_items(n=20, num_dimensions=3, max_demand=10, seed=42)

    greedy_bins = first_fit_decreasing(items, capacity)
    print_solution(greedy_bins, "Greedy (First-Fit Decreasing)")

    sa_bins, sa_cost = simulated_annealing(greedy_bins, capacity)
    print_solution(sa_bins, "Simulated Annealing (improved)")

    print(f"\nGreedy bins used: {len(greedy_bins)}")
    print(f"Simulated Annealing bins used: {len(sa_bins)}")