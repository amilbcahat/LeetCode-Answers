class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        #Crazy Solution - 
        #Keep track of the parity 
        #Solution - https://leetcode.com/problems/number-of-stable-subsequences/solutions/7187626/cpp-easy-code-dp-space-optimization-o-1
        mod = 10 ** 9 + 7
        e1 = e2 = o1 = o2 = 0

        for n in nums: 
            if n & 1 == 0: 
                new_e1 = (e1 + (o1 + o2 + 1)) % mod 
                new_e2 = (e1 + e2) % mod 
                e1 = new_e1
                e2 = new_e2
            else:
                new_o1 = (o1 + (e1 + e2 + 1)) % mod 
                new_o2 = (o1 + o2) % mod
                o1 = new_o1 
                o2 = new_o2

        return (e1 + e2 + o1 + o2) % mod


        # #just maintain states for previous parities
        # mod = 10 ** 9 + 7
        # # @lru_cache #This is very helpful, saved my time, use when hashmap cache gives issues! 
        # def dfs(i, prevPrevParity, prevParity): 
        #     if i >= len(nums): 
        #         return 1

        #     not_include = dfs(i + 1, prevPrevParity, prevParity)
        #     if prevParity != -1 and prevPrevParity != -1: 
        #         if (prevParity and prevPrevParity and nums[i] % 2 == 0) or (not prevParity and not prevPrevParity and not nums[i] % 2 == 0): 
        #             return not_include
                
        #     res = dfs(i + 1, prevParity, nums[i] % 2 == 0)
        #     res = (res + (not_include) % mod) % mod

        #     return res 

        # return dfs(0, -1, -1) - 1

        