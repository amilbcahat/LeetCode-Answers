class ExamTracker:
    def __init__(self):
        self.times = []
        self.preScore = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.preScore.append(self.preScore[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        rightIdx = -1 
        l = 0 
        r = len(self.times) - 1
        target = endTime
        while l <= r : 
            mid = (l + r) // 2
            if self.times[mid] <= target: 
                l = mid + 1
                rightIdx = mid
            else: 
                r = mid - 1

        leftIdx = -1

        l = 0 
        r = len(self.times) - 1
        target = startTime
        while l <= r: 
            mid = (l + r) // 2
            if self.times[mid] >= target: 
                r = mid - 1
                leftIdx = mid
            else: 
                l = mid + 1

        if leftIdx > rightIdx: 
            return 0 

        return self.preScore[rightIdx + 1] - self.preScore[leftIdx]
# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)