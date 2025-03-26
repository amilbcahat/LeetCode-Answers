class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftSum = 0
        for i, x in enumerate(nums): 
            rightSum = S - leftSum - x
            if leftSum == rightSum: 
                return i 
            leftSum += x 

        return -1