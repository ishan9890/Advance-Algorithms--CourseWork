class MinHeap:
    def __init__(self):
        self.data = []  

    def insert(self, key, name):
        self.data.append((key, name))
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i][0] < self.data[parent][0]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def peek_min(self):
        return self.data[0] if self.data else None

    def extract_min(self):
        if not self.data:
            return None
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return top

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left, right, smallest = 2 * i + 1, 2 * i + 2, i
            if left < n and self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < n and self.data[right][0] < self.data[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

    def is_empty(self):
        return len(self.data) == 0


if __name__ == "__main__":
    heap = MinHeap()
    cities = [(50, "CityA"), (30, "CityB"), (70, "CityC"), (20, "CityD"), (40, "CityE"), (10, "CityF")]
    for key, name in cities:
        heap.insert(key, name)

    print("Peek min:", heap.peek_min())

    print("Extracting all cities in order of nearest distance:")
    while not heap.is_empty():
        print(heap.extract_min())