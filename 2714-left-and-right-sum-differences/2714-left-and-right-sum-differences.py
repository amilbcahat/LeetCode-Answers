class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        S = sum(nums)
        leftSum = 0
        res = []
        for i, x in enumerate(nums): 
            rightSum = S - leftSum - x
            res.append(abs(leftSum - rightSum))
            leftSum += x
        return res
