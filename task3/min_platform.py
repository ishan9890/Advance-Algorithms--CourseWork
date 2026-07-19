def min_platforms(arrivals, departures):
    """
    Returns the minimum number of platforms required so that no train waits.
    arrivals, departures: lists of times (e.g. in 24hr int format like 900, 1015)
    """
    n = len(arrivals)
    arr = sorted(arrivals)
    dep = sorted(departures)

    platforms_needed = 0
    max_platforms = 0
    i, j = 0, 0  

    while i < n and j < n:
        if arr[i] <= dep[j]:
            # a train arrives before (or exactly when) another departs -> needs a platform
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            # a train departs before the next arrival -> frees a platform
            platforms_needed -= 1
            j += 1

    return max_platforms


def min_platforms_exact_bruteforce(arrivals, departures):
    """Brute-force O(n^2) cross-check: for every train's arrival time,
    count how many trains are simultaneously present."""
    n = len(arrivals)
    max_count = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if arrivals[j] <= arrivals[i] <= departures[j]:
                count += 1
        max_count = max(max_count, count)
    return max_count


if __name__ == "__main__":
    arrivals =   [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]

    result_greedy = min_platforms(arrivals, departures)
    result_brute = min_platforms_exact_bruteforce(arrivals, departures)

    print("Arrivals:  ", arrivals)
    print("Departures:", departures)
    print(f"\nMinimum platforms needed (greedy, O(n log n)): {result_greedy}")
    print(f"Minimum platforms needed (brute-force, O(n^2)):  {result_brute}")
    print(f"Results match: {result_greedy == result_brute}")