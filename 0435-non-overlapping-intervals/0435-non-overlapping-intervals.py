class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        cur = []
        prev = intervals[0]
        for start, end in intervals[1:]:
            cur = [start, end]
            if cur[0] < prev[1]:
                res += 1
                prev = [cur[0], min(cur[1], prev[1])]
            else:
                prev = cur

            
        return res