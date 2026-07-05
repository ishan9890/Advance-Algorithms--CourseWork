class AVLNode:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _h(self, node):
        return node.height if node else 0
    
    def _balance(self, node):
        return self._h(node.left) - self._h(node.right) if node else 0
    
    def _update(self, node):
        node.height = 1 + max(self._h(node.left), self._h(node.right))

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._update(y)
        self._update(x)
        return x
    
    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._update(x)
        self._update(y)
        return y
    
    def insert(self, key, name):
        self.root = self._insert(self.root, key, name)

    def _insert(self, node, key, name):
        if node is None:
            return AVLNode(key, name)
        if key < node.key:
            node.left = self._insert(node.left, key, name)
        else:
            node.right = self._insert(node.right, key, name)
        self._update(node)
        balance = self._balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
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
        
        self._update(node)
        balance = self._balance(node)

        if balance > 1 and self._balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance < -1 and self._balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance > 1 and self._balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node
    
if __name__ == "__main__":
    avl = AVLTree()
    cities = [(50, "CityA"), (30, "CityB"), (70, "CityC"), (20, "CityD"), (40, "CityE")]
    for key, name in cities:
        avl.insert(key, name)

    print("Search 40: ", avl.search(40).name)
    print("Root Key (after balancing): ", avl.root.key)
    print("Root height: ", avl.root.height)
    avl.delete(30)
    print("Search 30 after deletion: ", avl.search(30))
    print("Root height (after deletion): ", avl.root.height)