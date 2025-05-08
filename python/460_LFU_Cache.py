class Node:
    def __init__(self, key: int = -1, val: int = -1, next=None, prev=None):
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

    def first(self):
        return self.head.next
    
    def last(self):
        return self.tail.prev

    def empty(self):
        return self.head.next == self.tail and self.tail.prev == self.head

    def append(self, node):
        last = self.tail.prev
        last.next = node
        node.next = self.tail
        node.prev = last
        self.tail.prev = node
    
    def delete(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

class LFUCache:

    def __init__(self, capacity: int):
        self.memo = {}
        self.freqs = Counter()
        self.minf = 1
        self.freqdll = defaultdict(DLL)
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        # print(f"at get({key})")
        node = self.memo[key]
        oldf = self.freqs[key]
        self.freqs[key] += 1
        newf = self.freqs[key]
        # print(f"\tgot node with val {node.val}, oldf {oldf} and newf {newf}")

        self.freqdll[oldf].delete(node)
        self.freqdll[newf].append(node)

        if self.freqdll[oldf].empty() and oldf == self.minf:
            self.minf += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.memo:
            # print(f"at put({key}, {value}) where {key} is in the memo")
            node = self.memo[key]
            node.val = value
            oldf = self.freqs[key]
            self.freqs[key] += 1
            newf = self.freqs[key]

            self.freqdll[oldf].delete(node)
            self.freqdll[newf].append(node)

            if self.freqdll[oldf].empty() and self.minf == oldf:
                self.minf += 1
        else:
            # print(f"at put({key},{value}) where {key} is not in the memo")
            node = Node(key, value)
            self.memo[key] = node
            if len(self.memo) > self.cap:
                minnode = self.freqdll[self.minf].first()
                self.freqdll[self.minf].delete(minnode)
                self.freqs[minnode.key] -= 1
                if self.freqs[minnode.key] <= 0:
                    del self.freqs[minnode.key]
                del self.memo[minnode.key]
            
            self.minf = 1
            self.freqs[key] += 1
            self.freqdll[1].append(node)




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)