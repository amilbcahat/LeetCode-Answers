class Element: 
    def __init__(self, num, freq, seq_num): 
        self.num = num 
        self.freq = freq
        self.seq_num = seq_num

    def __lt__(self, other): 
        if self.freq != other.freq: 
            return self.freq > other.freq
        return self.seq_num > other.seq_num

class FreqStack:
    def __init__(self):
        self.seq_num = 0 
        self.freq_map = defaultdict(int)
        self.max_heap = []

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        heapq.heappush(self.max_heap, Element(val, self.freq_map[val], self.seq_num))
        self.seq_num += 1
        
    def pop(self) -> int:
        num = heapq.heappop(self.max_heap).num
        if self.freq_map[num] > 1 :
            self.freq_map[num] -= 1
        return num  


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()