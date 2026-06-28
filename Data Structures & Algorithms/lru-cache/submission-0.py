class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head_dummy = Node(None, None)
        self.tail_dummy = Node(None, None)
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy
        self.cache = {}
        self.capacity = capacity


    def update_mru(self, node: Node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        old = self.tail_dummy.prev
        old.next = node
        node.prev = old
        node.next = self.tail_dummy
        self.tail_dummy.prev = node

    def remove_lru(self):
        old = self.head_dummy.next
        old_next = old.next
        self.head_dummy.next = old_next
        old_next.prev = self.head_dummy
        old.next = None
        old.prev = None
        del self.cache[old.key]


    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        if node == -1:
            return -1
        self.update_mru(node)

        return node.value



    
    def put(self, key: int, value: int) -> None:

        node = self.cache.get(key, -1)
        if node == -1:
            if (len(self.cache) == self.capacity):
                self.remove_lru()

            new_node = Node(key, value)
            old = self.tail_dummy.prev
            old.next = new_node
            new_node.prev = old
            new_node.next = self.tail_dummy
            self.tail_dummy.prev = new_node
            self.cache[key] = new_node
        
        else:
            node.value = value
            self.update_mru(node)

            


