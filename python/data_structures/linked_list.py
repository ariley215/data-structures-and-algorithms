class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        values = ""
        current = self.head
        while current:
            values += f"{{ {current.value} }} -> "
            current = current.next
        values += "NULL"
        return values


    def insert_before(self, target, value):
        current = self.head
        while current.next:
            if current.next.value == target:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

    def kth_from_end(self,index):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        while current:
            if index == 0:
                return index.value




class TargetError:
    pass
