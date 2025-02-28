class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = []
        maxHeap = []

        freqMap = Counter(tasks)
        for key in freqMap: 
            heapq.heappush(maxHeap, (-freqMap[key], key))

        cooldown = deque()
        time = 0 
        print(maxHeap)
        while maxHeap or cooldown:
            # print(cooldown, time)
            if cooldown and cooldown[0][2] <=  time: 
                # print("cooldown over:",cooldown, time)
                cnt, ch, reqTime = cooldown.popleft()
                heapq.heappush(maxHeap, (-cnt, ch))

            if maxHeap:
                negCnt, trgt = heapq.heappop(maxHeap)
                count = -negCnt
                res.append(trgt)
                print(trgt)
                if count > 1: 
                    cooldown.append((count - 1, trgt, time + n + 1))
            else: 
                res.append("idle")

            time += 1

        print(res)
        return time

