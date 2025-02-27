class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        maxHeap = []
        freqMap = Counter(s)
        for key in freqMap: 
            heapq.heappush(maxHeap, (-freqMap[key], key)) #count, timer, key

        time = 0 
        res = []
        cooldown = deque()
        while len(res) < len(s): 
            if cooldown and cooldown[0][2] <= time: 
                cnt, ch, popTime = cooldown.popleft()
                heapq.heappush(maxHeap, (-cnt, ch))

            if not maxHeap: 
                return ""
                
            negCnt, ch = heapq.heappop(maxHeap)
            count = -negCnt
            res.append(ch)

            if count > 1: 
                cooldown.append((count - 1, ch, time + k))

            time += 1
        
        return ''.join(res) 
