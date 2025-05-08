class MyCircularQueue:

    def __init__(self, k: int):
        self.sz = 0
        self.head = self.tail = -1
        self.cap = k
        self.q = [-1] * self.cap

    def enQueue(self, value: int) -> bool:
        if self.sz == self.cap:
            return False
        self.tail = (self.tail + 1) % self.cap
        if self.head == -1:
            self.head = (self.head + 1) % self.cap
        self.q[self.tail] = value
        self.sz += 1
        # print(f"after insert {value}, q: {self.q}, tail: {self.tail}")

        return True


    def deQueue(self) -> bool:
        if self.sz == 0:
            return False
        self.q[self.head] = -1
        self.head = (self.head + 1) % self.cap
        self.sz -= 1
        # print(f"after delete, q: {self.q}, head: {self.head}")

        return True

    def Front(self) -> int:
        return self.q[self.head]

    def Rear(self) -> int:
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.sz == 0

    def isFull(self) -> bool:
        return self.sz == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()