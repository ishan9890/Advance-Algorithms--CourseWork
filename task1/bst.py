class BSTNode:
    def __init__(self, key, name):
        self.key = key
        self.left = None
        self.right = None
        self.name = name

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, name):
        self.root = self._insert(self.root, key, name)

    def _insert(self, node, key, name):
        if node is None:
            return BSTNode(key, name)
        if key < node.key:
            node.left = self._insert(node.left, key, name)
        else:
            node.right = self._insert(node.right, key, name)
        return node
    
    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = self._find_min(node.right)
            node.key, node.name = succ.key, succ.name
            node.right = self._delete(node.right, succ.key)
        return node
if __name__ == "__main__":
    bst = BST()
    cities = [(50, "CityA"), (30, "CityB"), (70, "CityC"), (20, "CityD"), (40, "CityE")]
    for key, name in cities:
        bst.insert(key, name)
    print("Search 40: ", bst.search(40).name)
    bst.delete(30)
    print("Search 30 after delete: ", bst.search(30))
