"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for emp in schedule: 
            for interval in emp:
                intervals.append([interval.start, interval.end])

        intervals.sort()
        output = [intervals[0]]

        #Merge Intervals
        for i in range(1, len(intervals)): 
            start,end = intervals[i]
            if start <= output[-1][1]: 
                output[-1][1] = max(end, output[-1][1])
            else: 
                output.append([start, end])
        
        #Check gaps 
        res = []
        for i in range(len(output) - 1):
            start , end = output[i]
            nextStart, nextEnd = output[i + 1]
            res.append(Interval(end , nextStart))

        return res