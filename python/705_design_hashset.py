class MyHashSet:
    SIZE: int = 10**6 + 1

    def __init__(self):
        self.vector = [-1] * MyHashSet.SIZE
    
    def _hash(self, key: int) -> int:
        return key % MyHashSet.SIZE

    def add(self, key: int) -> None:
        hashed = self._hash(key)
        self.vector[hashed] = key
        # print(f"in add: hashed: {hashed}, vector[hashed] = {self.vector[hashed]}")

    def remove(self, key: int) -> None:
        hashed = self._hash(key)
        self.vector[hashed] = -1
        # print(f"in remove: hashed: {hashed}, vector[hashed] = {self.vector[hashed]}")

    def contains(self, key: int) -> bool:
        hashed = self._hash(key)
        # print(f"in contains: hashed: {hashed}, vector[hashed] = {self.vector[hashed]}")
        return not self.vector[hashed] == -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)