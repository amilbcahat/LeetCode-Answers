class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        #Coin Change - Pattern

        #BitMask DP 
        res = []
        bit = 1 << k 
        mask = bit - 1 
        n = len(nums)
        for cap in range(1, n + 1): 
            b = 1
            for num in nums: 
                if num > cap:
                    num = cap

                b |= b << num

                if b & bit: 
                    res.append(True)
                    break
                b &= mask 
            else:
                res.append(False)
        return res

        # TLE 
        # def dfs(i, total): 
        #     if i <= len(nums2) and total == k: 
        #         return True 

        #     if i >= len(nums2): 
        #         return False

        #     if (i, total) in cache: 
        #         return cache[(i, total)]
                
        #     res = False 

        #     res = res or dfs(i + 1, total + nums2[i])
        #     res = res or dfs(i + 1, total)

        #     cache[(i, total)] = res
        #     return res

        # nums2 = [0] * len(nums)
        # n = len(nums)
        # ans = []

        # minElem = min(nums)
        # for x in range(1, n + 1): 
        #     if x <= minElem: 
        #         curSum = 0 
        #         found = False
        #         if n * x < k: 
        #             ans.append(found)
        #         elif (k % x) == 0:
        #             ans.append(True)
        #         else:
        #             ans.append(found)
                
        #     else:
        #         for i in range(n): 
        #             nums2[i] = min(x, nums[i])
        #         cache = {}
        #         ans.append(dfs(0, 0))

        # return ans