class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order_traversal(tree.root, "")
        elif traversal_type == "inorder":
            return self.in_order_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.post_order_traversal(tree.root, "")
        elif traversal_type == "levelorder":
            return self.level_order_traversal(tree.root, "")
        else:
            print("Traversal Type \"{}\" is not valid".format(traversal_type))

    def pre_order_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    def in_order_traversal(self, start, traversal):
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    def post_order_traversal(self, start, traversal):
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def level_order_traversal(self, start, traversal):
        if start:
            lst = [start.value]
            while lst:
                lst.append(start.left.value)
                lst.append(start.right.value)
                traversal += (str(lst.pop(0)) + "-")
                print(traversal)

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
