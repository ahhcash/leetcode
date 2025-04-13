class MyHashMap:
    SIZE: int = 10 ** 6 + 1
    
    def __init__(self):
        self.vector = [-1] * MyHashMap.SIZE    

    @staticmethod
    def _hash(key: int) -> int:
        return key % MyHashMap.SIZE

    def put(self, key: int, value: int) -> None:
        hashed = MyHashMap._hash(key)
        self.vector[hashed] = value

    def get(self, key: int) -> int:
        return self.vector[MyHashMap._hash(key)]

    def remove(self, key: int) -> None:
        self.vector[MyHashMap._hash(key)] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)