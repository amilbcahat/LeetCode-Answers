class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        start, end = meetings[0]

        #Merged Intervals
        merged = []
        merged.append(meetings[0])
        for i in range(1, len(meetings)):
            if merged[-1][1] >= meetings[i][0]: 
                merged[-1][1] = max(merged[-1][1], meetings[i][1])
            else: 
                merged.append(meetings[i])


        #Counted gaps at start, between and at end 
        res = merged[0][0] - 1 
        for i in range(1, len(merged)):
            if merged[i][0] > merged[i - 1][1]: 
                res += (merged[i][0] - merged[i - 1][1]) - 1
        res += (days - merged[-1][1])

        return res


        # for start, end in meetings: 

        # arr = [0] * (days + 2) 

        # for start, end in meetings: 
        #     arr[start] += 1
        #     arr[end + 1] -= 1 

        # curr = arr[0]
        # for i in range(len(arr)): 
        #     arr[i] += curr
        #     curr = arr[i]

        # res = 0 
        # for i in range(1, days + 1): 
        #     if arr[i] == 0: 
        #         res += 1
        # return res