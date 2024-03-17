class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #if and elif cases are when overlapping does happen 
            if newInterval[1] < intervals[i][0]:
                #End of newInterval is less than start of this interval , hence no insertion point 
                res.append(newInterval)
                #Add new one to first , then return with rest of intervals 
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                #Start of new interval is more than end of last this interval 
                #Append the existing interval and look for overlapping in rest of array 
                res.append(intervals[i])
            else : 
                #Overlapping happens , so we take min of start of both and max of end of both 
                #And look for more intervals that could be overlapped , to find the correct array result 
                newInterval = [min(newInterval[0] , intervals[i][0]) , max(newInterval[1] , intervals[i][1])]

        #Append newInterval , if the first if case does not run 
        res.append(newInterval)
        return res 