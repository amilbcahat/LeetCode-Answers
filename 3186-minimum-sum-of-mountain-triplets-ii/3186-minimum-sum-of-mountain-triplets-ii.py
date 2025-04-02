class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        #leftMin Prefixes 
        #rightMin Suffixes 
        #Then pivot around k 
        #Look over triplet i and ii , good intuition to build 
        n = len(nums)
        leftMin = [float("inf")]  * n 
        rightMin = [float("inf")] * n 

        for i in range(1, n): 
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
            rightMin[n - i - 1] = min(rightMin[n - i], nums[n - i])

        res = float("inf")
        for k in range(1, n - 1): 
            if leftMin[k] < nums[k] and nums[k] > rightMin[k]: 
                res = min(nums[k] + leftMin[k] + rightMin[k], res)

        return -1 if res == float("inf") else res