class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        @lru_cache
        def dfs(i, prevPrevParity, prevParity): 
            if i >= len(nums): 
                return 1

            # print(path, prevPrevParity, prevParity)
            not_include = dfs(i + 1, prevPrevParity, prevParity)
            if prevParity != -1 and prevPrevParity != -1: 
                if (prevParity and prevPrevParity and nums[i] % 2 == 0) or (not prevParity and not prevPrevParity and not nums[i] % 2 == 0): 
                    # print(path + [nums[i]], "discarded", prevParity, prevPrevParity, nums[i] % 2 != 0, )             
                    return not_include
                
            res = dfs(i + 1, prevParity, nums[i] % 2 == 0)
            res = (res + (not_include) % mod) % mod

            return res 

        return dfs(0, -1, -1) - 1

        