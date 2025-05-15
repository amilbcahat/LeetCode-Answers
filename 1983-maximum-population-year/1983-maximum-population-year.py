class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        timeline = [0] * 1000

        for start, end in logs: 
            st = start - 1950 
            ed = end - 1950 
            print(st, ed)
            timeline[st] += 1
            timeline[ed] -= 1

        for i in range(1, len(timeline)):
            timeline[i] += timeline[i - 1]

        maxVal = max(timeline)
        for i in range(len(timeline)):
            if maxVal == timeline[i]: 
                return i + 1950
