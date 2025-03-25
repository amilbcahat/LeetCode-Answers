class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        y = [[s[1], s[3]] for s in rectangles]
        x = [[s[0], s[2]] for s in rectangles]

        y.sort()
        x.sort()
        latest_end = -1
        newStart = 0
        for start, end in y: 
            if start >= latest_end: 
                newStart += 1
            latest_end = max(end, latest_end)


        if newStart >= 3:
            return True 

        latest_end = -1
        newStart = 0
        for start, end in x: 
            if start >= latest_end: 
                newStart += 1
            latest_end = max(end, latest_end)

        if newStart >= 3:
            return True 

        return False