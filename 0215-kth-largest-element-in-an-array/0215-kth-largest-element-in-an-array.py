class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxValue = max(nums)
        minValue = min(nums)
        count = [0] * ((maxValue - minValue) + 1)
        for num in nums: 
            count[num - minValue] += 1

        res = []
        for i in range(len(count)): 
            res = res + ([i + minValue] * count[i])

        return res[-k]

