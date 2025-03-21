class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        minDiff = float("inf")
        nums.sort()
        for i in range(len(nums) - 1): 
            minDiff = min(nums[i + 1] - nums[i], minDiff)

        res = []
        for i in range(len(nums) - 1): 
            if nums[i + 1] - nums[i] == minDiff: 
                res.append([nums[i], nums[i + 1]])
        
        return res       