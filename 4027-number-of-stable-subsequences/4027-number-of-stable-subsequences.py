class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # MLE with python
        mod = 10 ** 9 + 7
        n = len(nums)
        
        # Fixed cache array dimensions: [n+1][3][3] to handle -1,0,1 -> 0,1,2
        cache = [[[-1] * 3 for _ in range(3)] for _ in range(n + 1)]
        
        def dfs(i, prevPrevParity, prevParity):
            if i >= len(nums):
                return 1
            
            # Map -1,0,1 to 0,1,2 for array indexing
            pp_idx = prevPrevParity + 1
            p_idx = prevParity + 1
            
            # Fixed cache check
            if cache[i][pp_idx][p_idx] != -1:
                return cache[i][pp_idx][p_idx]
            
            # print(path, prevPrevParity, prevParity)
            if prevParity != -1 and prevPrevParity != -1:
                if (prevParity and prevPrevParity and nums[i] % 2 == 0) or (not prevParity and not prevPrevParity and not nums[i] % 2 == 0):
                    # print(path + [nums[i]], "discarded", prevParity, prevPrevParity, nums[i] % 2 != 0, )
                    cache[i][pp_idx][p_idx] = dfs(i + 1, prevPrevParity, prevParity)
                    return cache[i][pp_idx][p_idx]
                    
            res = dfs(i + 1, prevParity, nums[i] % 2 == 0)
            res = (res + (dfs(i + 1, prevPrevParity, prevParity) % mod)) % mod
            
            cache[i][pp_idx][p_idx] = res
            return res
        
        return dfs(0, -1, -1) - 1