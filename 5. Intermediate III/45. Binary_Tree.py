class Tree:
    def __init__(self, left, value, right):
        self.left = left
        self.value = value
        self.right = right

tree = Tree(Tree("a", "b", "c"), "d", Tree("e", "f", 'g'))

print(tree.left.left)
print(tree.left.value)
print(tree.left.right)
print(tree.value)
print(tree.right.left)
print(tree.right.value)
print(tree.right.right)

# To do: Create functions to insert, display, and delete elements in a binary tree.