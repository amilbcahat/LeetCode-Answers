class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        cache = {}
        def dfs(i):
            if i >= len(questions):
                return 0 

            if i in cache : 
                return cache[i]

            #Take Question#
            
            take = questions[i][0] + dfs(i + (questions[i][1] + 1))

            #Dont take Question 
            skip = dfs(i + 1)

            cache[i] = max(take , skip)

            return cache[i]

        return dfs(0)