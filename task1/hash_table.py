class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, name):
        idx = self._hash(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                pair[1] = name   # update existing
                return
        self.buckets[idx].append([key, name])

    def search(self, key):
        idx = self._hash(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                return pair
        return None

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return True
        return False

    def load_factor(self):
        total_items = sum(len(b) for b in self.buckets)
        return total_items / self.size


if __name__ == "__main__":
    ht = HashTable(size=16)
    cities = [("CityA", 50), ("CityB", 30), ("CityC", 70), ("CityD", 20), ("CityE", 40)]

    for name, distance in cities:
        ht.insert(name, distance)

    print("Search CityC:", ht.search("CityC"))
    print("Load factor:", ht.load_factor())

    ht.delete("CityB")
    print("Search CityB after delete:", ht.search("CityB"))
    print("Load factor after delete:", ht.load_factor())
    