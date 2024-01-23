from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        while not inbox.is_empty():
            popped = inbox.pop()
            outbox.push(popped)

    dequeued = outbox.pop()

    while not outbox.is_empty():
        popped = self.outbox.pop()
        self.inbox.push(popped)
