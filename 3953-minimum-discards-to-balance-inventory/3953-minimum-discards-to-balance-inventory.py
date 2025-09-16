class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        l = 0 
        ans = 0
        freqMap = defaultdict(int)
        kept = deque()
        for i, item in enumerate(arrivals): 
            day = i + 1 
            window_start = max(1, day - w + 1)
            while kept and kept[0][0] < window_start: 
                _, itemVal = kept.popleft()
                freqMap[itemVal] -= 1
                if freqMap[itemVal] == 0: 
                    del freqMap[itemVal]

            if freqMap[item] + 1 > m: 
                ans += 1
            else: 
                kept.append((day, item))
                freqMap[item] += 1


        return ans 