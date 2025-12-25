class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        #Amazon OA same problem was asked 
        #Very beautiful question

        badMap = defaultdict(int)
        goodMap = defaultdict(list)
        maxHeap = []
        for i, n in enumerate(nums): 
            if n == forbidden[i]:
                #bad
                badMap[n] += 1
            else: 
                goodMap[n].append(forbidden[i])


        if not badMap:
            return 0

        sub = badMap.values()
        if len(nums) % 2 == 0 and max(sub) <= len(nums) / 3 and sum(sub) == len(nums):
            return len(nums) // 2

        for k, v in badMap.items(): 
            heapq.heappush(maxHeap, (-v, k))

        swaps = 0
        while len(maxHeap) > 1:
            fre1, tp1 = heapq.heappop(maxHeap)
            fre2, tp2 = heapq.heappop(maxHeap)
            fre1, fre2 = -fre1, -fre2
            pairs = min(fre1, fre2)
            swaps += pairs

            for _ in range(pairs): 
                goodMap[tp1].append(tp2)
                goodMap[tp2].append(tp1)

            fre1 -= pairs
            fre2 -= pairs

            if fre1 > 0: 
                heapq.heappush(maxHeap, (-fre1, tp1))
            if fre2 > 0: 
                heapq.heappush(maxHeap, (-fre2, tp2))

        if not maxHeap: 
            return swaps

        #Only one would be left here 
        lastFreq, lastVal = heapq.heappop(maxHeap)
        lastFreq = -lastFreq

        for key in goodMap:
            if lastFreq <= 0:
                break
            for af in goodMap[key]:
                if lastVal != af and key != lastVal:
                    lastFreq -= 1 
                    swaps += 1
                    print(key, af)

                    if lastFreq <= 0:
                        return swaps 

        return swaps if lastFreq <= 0 else -1 


