class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.q1active = True

    def push(self, x: int) -> None:
        if self.q1active:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        if self.q1active:
            while not len(self.q1) == 1:
                self.q2.append(self.q1.popleft())
            self.q1active = False
            return self.q1.popleft()
        else:
            while not len(self.q2) == 1:
                self.q1.append(self.q2.popleft())
            self.q1active = True
            return self.q2.popleft()

    def top(self) -> int:
        if self.q1active:
            return self.q1[-1]
        return self.q2[-1]

    def empty(self) -> bool:
        if self.q1active:
            return len(self.q1) == 0
        return len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()