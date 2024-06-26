class MyStack:

    def __init__(self):
        self.mainqueue = deque()
        self.auxqueue = deque()

    def push(self, x: int) -> None:
        self.mainqueue.append(x)
       
        
    #Major intuition here is that , in stack for every operation we deal with top only , so we need to preserver that 
    #SO for Pop and Top , from mainqueue we transfer all element to auxqueue , except the last , which will be considered as top of stack 
    def pop(self) -> int:
        for i in range(len(self.mainqueue)-1):
            x = self.mainqueue.popleft()
            self.auxqueue.append(x)
        #In pop we remove the element 
        last = self.mainqueue.popleft()
        #And restore the mainqueue by swapping it 
        self.mainqueue  , self.auxqueue = self.auxqueue , self.mainqueue
        return last 
        

    def top(self) -> int:
        for i in range(len(self.mainqueue)-1):
            x = self.mainqueue.popleft()
            self.auxqueue.append(x)
        #In top , we fetch the top of stack and append back to aux 
        top = self.mainqueue.popleft()
        self.auxqueue.append(top)
        #Then restore mainqueue by swapping it 
        self.mainqueue  , self.auxqueue = self.auxqueue , self.mainqueue
        return top 
        

    def empty(self) -> bool:
        return len(self.mainqueue) == 0 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()