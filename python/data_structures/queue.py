from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_node = Node(value)
        # if Queue is empty
        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            # point the queue's self.back to our new node. Update the pointer!
            self.back = new_node

    def dequeue(self):
        """
        removes front node from the queue and returns its value
        """
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        dequeue_value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.back = None
        return dequeue_value

    def peek(self):
        if self.front is None:
            self.back = None
            raise InvalidOperationError("Method not allowed on empty collection")
        peek_front_value = self.front.value
        peek_back_value = self.back.value
        return peek_back_value and peek_front_value

    def is_empty(self):
        if self.front is None:
            if self.back is None:
                return True
