class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = score.copy()
        arr.sort()

        indexMap = {}
        print(arr)
        for i in range(len(arr) - 1 , -1  ,-1):
            indexMap[arr[i]] = len(arr) - i 

        print(indexMap)

        
        for i in range(len(arr)) : 
            if indexMap[score[i]] == 1 : 
                score[i] = "Gold Medal"
            elif indexMap[score[i]] == 2 :
                score[i] = "Silver Medal"
            elif indexMap[score[i]] == 3 : 
                score[i] = "Bronze Medal"
            else:
                score[i] = str(indexMap[score[i]])
        

        return score 