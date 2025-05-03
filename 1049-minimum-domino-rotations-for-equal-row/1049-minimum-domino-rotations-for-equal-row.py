class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        countMapT = Counter(tops)
        countMapB = Counter(bottoms)
        maxCountT = max(countMapT.values())
        maxCountB = max(countMapB.values())

        maxCountVarT = -1 
        maxCountVarB = -1 

        for key in countMapT: 
            if countMapT[key] == maxCountT: 
                maxCountVarT = key

        for key in countMapB: 
            if countMapB[key] == maxCountB: 
                maxCountVarB = key

        opsT = 0 
        opsB = 0 

        
        for i in range(len(tops)): 
            if tops[i] != maxCountVarT and bottoms[i] == maxCountVarT: 
                opsT += 1

        for i in range(len(bottoms)): 
            if bottoms[i] != maxCountVarB and tops[i] == maxCountVarB: 
                opsB += 1

        opsT = -1 if opsT + maxCountT != len(tops) else opsT
        opsB = -1 if opsB + maxCountB != len(bottoms) else opsB

        return min(opsB, opsT) if opsT > 0 and opsB > 0 else  opsT if opsT > 0 else opsB