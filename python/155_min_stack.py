class MinStack:

    def __init__(self):
        self.mins = []
        self.st = []


    def push(self, val: int) -> None:
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)
        
        self.st.append(val)

    def pop(self) -> None:
        if self.st[-1] == self.mins[-1]:
            self.mins.pop()
        self.st.pop()


    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()