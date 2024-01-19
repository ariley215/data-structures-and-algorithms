class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def zip_lists(a, b):
        current_a = a
        current_b = b
        while current_a and current_b:
            next_a = current_a.next
            next_b = current_b.next

            current_a.next = current_b
            current_b.next = next_a

            current_a = next_a
            current_b = next_b

            return a


