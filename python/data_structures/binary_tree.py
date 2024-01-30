class BinaryTree:
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

    def find_maximum_value(self):
        if self.root is None:
            return None

        max_value_list = [float('-inf')]

        def mod_pre_order(node):

            if node:

                max_value_list[0] = max(max_value_list[0], node.value)


                mod_pre_order(node.left)
                mod_pre_order(node.right)


        mod_pre_order(self.root)

        return max_value_list[0]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
