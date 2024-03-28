class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0 
        count = defaultdict(int)

        for r in range(len(nums)):
            count[nums[r]] +=  1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1

            res = max(r - l + 1 , res)

        return res