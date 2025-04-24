class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indices = {}
        self.i = 0

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.values.append(val)
        self.indices[val] = self.i
        self.i += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        self.indices[self.values[-1]] = self.indices[val]
        self.values[-1], self.values[self.indices[val]] = self.values[self.indices[val]], self.values[-1]
        self.values.pop()
        self.i -= 1
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()