class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]: 
            self.min_stack.append([val , 1])

        elif val == self.min_stack[-1][0]: 
            self.min_stack[-1][1] += 1

        
    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1][0]: 
            self.min_stack[-1][1] -= 1

        if self.min_stack[-1][1] == 0: 
            self.min_stack.pop()
        
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()