class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        cur = 1
        for r in range(len(nums)):
            cur *= nums[r]
            while l <= r and cur >= k:
                cur //= nums[l]
                l +=1

            res += (r - l + 1)

        return res