class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return None

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                last_node = self.tail.prev
                self._remove_node(last_node)
                del self.cache[last_node.key]

            new_node = Node(key, value)
            self._add_node(new_node)
            self.cache[key] = new_node
lru = LRUCache(3)
lru.put(1, 'One')
lru.put(2, 'Two')
lru.put(3, 'Three')
print(lru.get(1)) 
lru.put(4, 'Four')
print(lru.get(2)) 
