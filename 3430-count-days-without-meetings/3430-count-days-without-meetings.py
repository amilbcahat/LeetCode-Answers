class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        start, end = meetings[0]
        here = []
        here.append(meetings[0])
        for i in range(1, len(meetings)):
            if here[-1][1] >= meetings[i][0]: 
                here[-1][1] = max(here[-1][1], meetings[i][1])
            else: 
                here.append(meetings[i])

        res = here[0][0] - 1 
        for i in range(1, len(here)):
            if here[i][0] > here[i - 1][1]: 
                res += (here[i][0] - here[i - 1][1]) - 1
        res += (days - here[-1][1])

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