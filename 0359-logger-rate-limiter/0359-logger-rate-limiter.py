class Logger:
    def __init__(self):
        self.nextAllowedLog = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.nextAllowedLog: 
            self.nextAllowedLog[message] = timestamp + 10
            return True 

        if self.nextAllowedLog[message] <= timestamp: 
            self.nextAllowedLog[message] = (timestamp + 10)
            return True

        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)