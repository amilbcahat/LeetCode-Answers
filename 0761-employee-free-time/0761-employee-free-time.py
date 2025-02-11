"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        #Heap
        free_gaps = []
        pq = []
        for i in range(len(schedule)): 
            for j in range(len(schedule[i])): 
                interval = schedule[i][j]
                pq.append([interval.start, i, j]) #start , emp_id , idx of emp of schedule

        heapq.heapify(pq)
        lastEndTime = pq[0][0]
        while pq: 
            start, emp_id, sch_idx = heapq.heappop(pq)
            cur_interval = schedule[emp_id][sch_idx]
            if lastEndTime < start:
                free_gaps.append(Interval(lastEndTime, start))

            lastEndTime = max(lastEndTime, cur_interval.end)
            nxt_sch_idx = sch_idx + 1
            if nxt_sch_idx < len(schedule[emp_id]):
                nxt_interval = schedule[emp_id][nxt_sch_idx]
                heapq.heappush(pq, [nxt_interval.start, emp_id , nxt_sch_idx])

        return free_gaps
        # intervals = []
        # for emp in schedule: 
        #     for interval in emp:
        #         intervals.append([interval.start, interval.end])

        # intervals.sort()
        # output = [intervals[0]]

        # #Merge Intervals
        # for i in range(1, len(intervals)): 
        #     start,end = intervals[i]
        #     if start <= output[-1][1]: 
        #         output[-1][1] = max(end, output[-1][1])
        #     else: 
        #         output.append([start, end])
        
        # #Check gaps 
        # res = []
        # for i in range(len(output) - 1):
        #     start , end = output[i]
        #     nextStart, nextEnd = output[i + 1]
        #     res.append(Interval(end , nextStart))

        # return res