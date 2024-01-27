from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node

        def traverse(node, add_node):
            if node is None:
                return
            if add_node.value < node.value:
                if node.left is None:
                    node.left = add_node
                else:
                    traverse(node.left, add_node)
            elif add_node.value > node.value:
                if node.right is None:
                    node.right = add_node
                else:
                    traverse(node.right, add_node)

        traverse(self.root, node)

    def contains(self, value):
        target_value = value

        if self.root is None:
            return False

        def check_tree(node_to_ask, target_value):
            if node_to_ask is None:
                return False
            if target_value < node_to_ask.value:
                return check_tree(node_to_ask.left, target_value)

            elif target_value > node_to_ask.value:
                return check_tree(node_to_ask.right, target_value)
            elif target_value == node_to_ask.value:
                return True

        return check_tree(self.root, target_value)






