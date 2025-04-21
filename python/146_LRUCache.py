class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.memo = {}
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    @staticmethod
    def _delete_node(node: Node) -> None:
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before
    
    def _append(self, node: Node) -> None:
        last =self.tail.prev
        last.next = node
        node.next = self.tail
        node.prev = last
        self.tail.prev = node

    def get(self, key: int) -> int:
        node = self.memo.get(key, None)
        if not node:
            return -1
        LRUCache._delete_node(node)
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            node = self.memo[key]
            LRUCache._delete_node(node)
        
        node = Node(key=key, val=value)
        self.memo[key] = node
        if self.cap < len(self.memo):
            first = self.head.next
            LRUCache._delete_node(first)
            del self.memo[first.key]
        
        self._append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)