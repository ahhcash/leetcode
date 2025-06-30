class Node:
    def __init__(self, key: int = -1, val: int = -1, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def delete(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dll = DLL()
        # print(f"caapacity = {capacity}")

    def get(self, key: int) -> int:
        # print(f"trying get({key})")
        if key not in self.cache: return -1
        node = self.cache[key]
        self.dll.delete(node)
        self.dll.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # print(f"trying put({key}, {value})")
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.dll.delete(node)
            self.dll.append(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                lru = self.dll.head.next
                self.dll.delete(lru)
                del self.cache[lru.key]
            self.dll.append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)