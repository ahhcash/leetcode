class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

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
    
    @staticmethod
    def delete(node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.freqmap = defaultdict(int)
        self.freqcounts = defaultdict(int)
        self.freqdll = defaultdict(DLL)
        self.minf = 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.freqcounts[self.freqmap[key]] -= 1
        if self.freqcounts[self.freqmap[key]] <= 0:
            del self.freqcounts[self.freqmap[key]]
        
        DLL.delete(node)

        if self.minf == self.freqmap[key] and self.freqcounts[self.freqmap[key]] == 0:
            self.minf += 1
        
        self.freqmap[key] += 1
        self.freqcounts[self.freqmap[key]] += 1
        self.freqdll[self.freqmap[key]].append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            DLL.delete(node)
            self.freqcounts[self.freqmap[key]] -= 1
            if self.freqcounts[self.freqmap[key]] <= 0:
                del self.freqcounts[self.freqmap[key]]
            
            if self.minf == self.freqmap[key] and self.freqcounts[self.freqmap[key]] == 0:
                self.minf += 1
            
            self.freqmap[key] += 1
            self.freqcounts[self.freqmap[key]] += 1
            self.freqdll[self.freqmap[key]].append(node)
            node.val = value
        else:
            node = Node(key, value)
            self.cache[key] = node
            if len(self.cache) > self.cap:
                # time to evict
                dll = self.freqdll[self.minf]
                first = dll.head.next
                DLL.delete(first)
                del self.cache[first.key]
                self.freqcounts[self.freqmap[first.key]] -= 1
                if self.freqcounts[self.freqmap[first.key]] <= 0:
                    del self.freqcounts[self.freqmap[first.key]]
                del self.freqmap[first.key]
            
            self.minf = 1
            self.freqmap[key] = 1
            self.freqcounts[1] += 1
            self.freqdll[1].append(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)