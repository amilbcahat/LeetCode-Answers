class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        #Read the Hints , should be clear 
        N = len(nums)
        res = []
        prefixSum = 0
        suffixSum = 0
        total = sum(nums)
        for i in range(len(nums)):
            prefixSum += nums[i] 
            suffixSum = total - prefixSum
            left = (nums[i] * i) - (prefixSum - nums[i])
            right = suffixSum - (nums[i] * (N - i - 1))
            res.append(left + right)
        
        return res
