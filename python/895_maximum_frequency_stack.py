class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.freqtoitems = defaultdict(list)
        self.maxf = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.freqtoitems[self.freq[val]].append(val)
        if self.freq[val] > self.maxf:
            self.maxf = self.freq[val]

    def pop(self) -> int:
        val = self.freqtoitems[self.maxf].pop()
        self.freq[val] -= 1
        if not self.freqtoitems[self.maxf]:
            self.maxf -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()