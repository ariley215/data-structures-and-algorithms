from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """ """

    def __init__(self):
        self.top = None
        pass

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        pop_value = self.top.value
        self.top = self.top.next
        return pop_value

    def is_empty(self):
        if self.top is None:
            return True

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        peek_value = self.top.value
        return peek_value
