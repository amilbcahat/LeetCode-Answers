class MyQueue:

    def __init__(self):
        self.s1 = [] #Stack used for pushing 
        self.s2 = [] #Stack used for popping 

    def push(self, x: int) -> None:
        #Pushing is simple and a O(1) operation
        self.s1.append(x)

    def pop(self) -> int:
        #Popping is difficult and an amortized O(1) solution 
        #On the first pop all the elements and pushed to Stack used for popping , and then we pop from there , since transfering element can be costly , if we do it each time 
        if not self.s2 : 
            while self.s1 : 
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
        

    def peek(self) -> int:
        #We do same for peek as we had done for pop
        if not self.s2 : 
            while self.s1 : 
                self.s2.append(self.s1.pop())
        
        return self.s2[-1]
        

    def empty(self) -> bool:
        #Checks if elements are empty in both stacks !
        return max(len(self.s1) , len(self.s2)) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()