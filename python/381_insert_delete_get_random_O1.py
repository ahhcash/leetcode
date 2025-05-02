class RandomizedCollection:

    def __init__(self):
        self.memo = []
        self.indices = defaultdict(set)
        self.i = 0

    def insert(self, val: int) -> bool:
        self.memo.append(val)
        self.indices[val].add(len(self.memo) - 1)
        return len(self.indices[val]) == 1


    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False

        idx_to_remove, last = self.indices[val].pop(), self.memo[-1]

        self.memo[idx_to_remove] = last
        self.indices[last].add(idx_to_remove)
        self.indices[last].discard(len(self.memo) - 1)
        
        self.memo.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.memo)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()