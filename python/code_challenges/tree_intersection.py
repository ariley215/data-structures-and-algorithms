from data_structures.hashtable import HashTable


def tree_intersection(tree_one, tree_two):
    hashtable = HashTable()
    common_values = []
    # traverse through the first tree and add the values to the hashtable
    def traverse_first(root):
        if root:
            if root.value not in hashtable:
                hashtable[root.value] = 1
            else:
                hashtable[root.value] =+ 1
            traverse_first(root.right)
            traverse_first(root.left)

    def traverse_second(root):
        if root:
            if root.value in hashtable and hashtable[root.value] > 1:
                common_values.append(root.value)
                hashtable[root.value] -= 1
            traverse_second(root.right)
            traverse_second(root.left)

    traverse_first(tree_one)
    traverse_second(tree_two)
    return common_values




