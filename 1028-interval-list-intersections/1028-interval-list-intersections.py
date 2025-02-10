class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 , p2 = 0 , 0 
        res = []
        def greedyChoice(p1, p2):
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            elif firstList[p1][1] > secondList[p2][1]:
                p2 += 1
            else: 
                p1 += 1
                p2 += 1
            return p1, p2

        while p1 < len(firstList) and p2 < len(secondList):
            if max(firstList[p1][0], secondList[p2][0]) <= min(firstList[p1][1], secondList[p2][1]):
                #overlapped !!
                res.append([max(firstList[p1][0], secondList[p2][0]), min(firstList[p1][1], secondList[p2][1])])
                p1, p2 = greedyChoice(p1, p2)
            else: 
                p1, p2 = greedyChoice(p1, p2)

        return res