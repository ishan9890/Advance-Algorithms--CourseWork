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