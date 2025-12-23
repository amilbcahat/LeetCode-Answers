class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = Counter(tasks)
        maxHeap = []

        t = 0
        for key, val in freqMap.items():
            heapq.heappush(maxHeap, (-val, key))

        cooldown = deque()
        res = []
        while maxHeap or cooldown: 
            while cooldown and cooldown[0][2] <= t: 
                cnt, ch, reqTime = cooldown.popleft()
                heapq.heappush(maxHeap, (-cnt, ch))

            if maxHeap: 
                freq, trgt = heapq.heappop(maxHeap)
                freq = -freq 
                res.append(trgt)
                if freq > 1 :
                    cooldown.append((freq - 1, trgt, t + n + 1))

            t += 1

        print(res)
        return t 