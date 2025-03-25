class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        y = [[s[1], s[3]] for s in rectangles]
        x = [[s[0], s[2]] for s in rectangles]

        y.sort()
        x.sort()

        #After merging, check 
        latest_end = -1
        sections = 0
        for start, end in y: 
            if start >= latest_end: 
                sections += 1
            latest_end = max(end, latest_end)

        if sections >= 3:
            return True 

        latest_end = -1
        sections = 0
        for start, end in x: 
            if start >= latest_end: 
                sections += 1
            latest_end = max(end, latest_end)

        if sections >= 3:
            return True 

        return False