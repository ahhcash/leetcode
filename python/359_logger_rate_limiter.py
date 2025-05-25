class Logger:

    def __init__(self):
        self.next = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.next or self.next[message] <= timestamp:
            self.next[message] = timestamp + 10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)