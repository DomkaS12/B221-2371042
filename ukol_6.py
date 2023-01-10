class Node:
    def __init__(self, data=None, left=None, right=None, balance=0, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.balance = balance

    def insert(self, data):
        if (data == None):
            return
        if (not self.getRoot()):
            self.setRoot(AVL_tree.AVL_node(data=data))
            return
        else:
            self._done = 0
            self.recursiveInsert(self.getRoot(), data)
            delattr(self, "_done")
            return
        pass

    @staticmethod
    def print_tree(tree):
        pass

    @staticmethod
    def in_order_traversal(tree):
        pass

    @staticmethod
    def max_depth(tree):
        pass

    @staticmethod
    def contains(tree, data):
        pass

tree = Node()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

assert tree.in_order_traversal(tree) == [1, 2, 3, 4, 5, 6, 7]
assert tree.contains(tree, 3)
assert not tree.contains(tree, 20)
assert tree.max_depth(tree) <= 2

tree = Node()

tree.insert(2)
tree.insert(10)
tree.insert(3)
tree.insert(5)
tree.insert(100)

assert tree.max_depth(tree) <= 2