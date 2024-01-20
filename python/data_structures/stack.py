from data_structures.linked_list import Node


class Stack:
    """

    """

    def __init__(self):
        self.top = None
        pass

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        pop_value = self.top.value
        self.pop = self.top.next
        return pop_value

