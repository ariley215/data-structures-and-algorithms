from .linked_list import LinkedList
class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % self.size

        return index

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self.bucket[index] = bucket

        current = bucket.head
        while current:
            insert_drop = current.value
            if insert_drop[0] == key:
                insert_drop[1] = value
                return
        drop = [key, value]
        bucket.insert(drop)

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        if bucket is None:
            return None
        current = bucket.head
        while current:
            drop = current.value #key value pair
            if drop[0] == key:
                return drop[1]
            current = current.next
        return None

    def has(self, key):
        for bucket in self.buckets:
            if bucket:  # bucket is a linked list self.buckets is list of linked lists
                current = bucket.head
                while current:
                    drop = current.value
                    if drop[0] == key:
                        return True
                    current = current.next
                return False

    def keys(self):
        key_list = [] # list of strings
        for bucket in self.buckets:
            if bucket: # bucket is a linked list self.buckets is list of linked lists
                current = bucket.head
                while current:
                    drop = current.value
                    key_list.append(drop[0])
                    current = current.next
        return key_list
