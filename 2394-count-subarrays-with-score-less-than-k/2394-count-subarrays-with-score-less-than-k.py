class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        def atmost(k): 
            n = len(nums)
            res , total = 0 , 0
            l = 0
            for r in range(len(nums)): 
                total += nums[r]
                while l <= r and total * (r - l + 1) >= k: 
                    total -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res

        # def atmost(k): 
            # l = 0 
            # total = 0
            # prevLen = 1
            # res = 0
            # for r in range(len(nums)): 
            #     curLen = (r - l + 1)
            #     total = total / (1 if prevLen == 0 else prevLen)
            #     total = total * curLen + nums[r] * curLen

            #     # print(nums[l: r + 1], "outside", total, curLen, prevLen)
            #     while l <= r and total >= k: 
            #         total = total - nums[l] * curLen
            #         total = total / curLen 
            #         total = total * prevLen
            #         l += 1
            #         curLen -= 1
            #         prevLen -= 1
            #         # curLen = (r - l + 1)
            #         # prevLen = curLen
            #         # print(nums[l: r + 1], total, curLen, prevLen)

            #     prevLen = curLen
            #     res += curLen
            #     # print(nums[l: r + 1], total)

            # return res

        return atmost(k)