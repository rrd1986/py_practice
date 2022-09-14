class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
 
    # most recently used key willbe saved in the head always
    def addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next= node

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            result = node.value
            self.delete(node)
            self.addToHead(node)
            return result
        return -1

    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.delete(node)
            self.addToHead(node)
        else:
            node = Node(key, value)
            if self.count < self.capacity:
                self.map[key] = node
                self.count += 1
                self.addToHead(node)
            else:
                del self.map[self.tail.prev.value]
                self.delete(self.tail.prev)
                self.addToHead(node)        


