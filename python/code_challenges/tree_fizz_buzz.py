from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(kary_tree):
    if not kary_tree.root:
        return KaryTree()

    def fizz_buzz(value):
        value = Node.value

        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    def copy_tree(node):
        new_node = Node(fizz_buzz(node.value))
        for child in Node.children:
            new_node.children.append(copy_tree(child))
        return new_node
    new_root = copy_tree(kary_tree.root)
    return KaryTree(new_root)
