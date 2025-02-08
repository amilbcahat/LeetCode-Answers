class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0 
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < prev[1]: 
                res += 1 
                prev = [curr[0] , min(prev[1], curr[1])]
            else:
                prev = curr
        
        return res #basically just remove overlaps