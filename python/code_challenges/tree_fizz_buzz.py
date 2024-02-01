from data_structures.kary_tree import KaryTree, Node, Queue


def fizz_buzz_tree(kary_tree):
    if kary_tree.root is None:
        return None

    clone_root = Node(kary_tree.root.value, kary_tree.root.children.copy())

    while Queue:
        current, clone = Queue.pop(0)

        if current.value % 3 == 0 and current.value % 5 == 0:
            clone.value = "FizzBuzz"
        if current.value % 3 == 0:
            clone.value = "Fizz"
        if current.value % 5 == 0:
            clone.value = "Buzz"
        else:
            clone.value = str(current.value)

    for i, child in enumerate(current.children):
        clone_child = Node(None)
        clone.children[i] = clone_child
        Queue.append((child, clone_child))
    return KaryTree(root=clone_root)
