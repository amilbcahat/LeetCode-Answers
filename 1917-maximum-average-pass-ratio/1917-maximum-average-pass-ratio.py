class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        for stu, total in classes: 
            cur_val = (stu/ total)
            profit = ((stu + 1) / (total + 1)) - cur_val
            heapq.heappush(maxHeap, (-1 * profit, stu, total))

        while extraStudents: 
            profit, stu, total = heapq.heappop(maxHeap)
            stu = stu + 1
            total = total + 1
            new_profit = ((stu + 1) / (total + 1)) - (stu / total)
            heapq.heappush(maxHeap, (-1 * new_profit, stu, total))
            extraStudents -= 1

        total_avg = 0
        for profit, finalStu, finalTotal in maxHeap: 
            total_avg += (finalStu/ finalTotal)

        return total_avg / len(maxHeap)

