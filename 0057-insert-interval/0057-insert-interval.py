class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                #beech mai nhi padega 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: 
                #yaha overlap nhi hua but open for merging if possible 
                res.append(intervals[i])
            else: 
                #jab overlapping ho hie 
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)
        return res 



                



