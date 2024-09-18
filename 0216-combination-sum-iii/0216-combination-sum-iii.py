class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1 , 2 , 3, 4, 5, 6, 7, 8, 9]
        res = []
        def dfs(i , curElem , curSum): 
            if i >= len(nums) and len(curElem) == k and curSum == n :
                res.append(curElem.copy())
                return 

            if i >= len(nums) or curSum > n : 
                return 
            

            dfs(i + 1 , curElem + [nums[i]] , curSum + nums[i])
            dfs(i + 1 , curElem , curSum)

        dfs(0 , [] , 0)

        return res


