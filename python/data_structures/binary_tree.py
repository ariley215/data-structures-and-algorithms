class BinaryTree():
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None



    def pre_order(self):
        def traverse(node):
            """
            return: my node value + left node values + right node values


            """
            if node is None:
                return []

            my_value = [node.value]
            left_node_values = traverse(node.left)
            right_node_values = traverse(node.right)

            return my_value + left_node_values + right_node_values

        return traverse(self.root)

    def in_order(self):
        def traverse(node):
            """
            return: left node values + my node value + right node values


            """
            if node is None:
                return []

            my_value = [node.value]
            left_node_values = traverse(node.left)
            right_node_values = traverse(node.right)

            return left_node_values + my_value + right_node_values

        return traverse(self.root)

    def post_order(self):
        def traverse(node):
            """
            return: right node values + left node values + my node value


            """
            if node is None:
                return []

            my_value = [node.value]
            left_node_values = traverse(node.left)
            right_node_values = traverse(node.right)

            return left_node_values + right_node_values + my_value

        return traverse(self.root)

    def find_max


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


