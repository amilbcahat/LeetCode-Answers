class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxElem = [float("-inf"), -1]
        minElem = [float("inf"), 1]
        for i in range(len(nums)): 
            if maxElem[0] < nums[i]:
                maxElem = [nums[i], i]
            if minElem[0] > nums[i]: 
                minElem = [nums[i], i]

        deletions = 0 
        removeFromleft = max(maxElem[1] + 1, minElem[1] + 1)
        removeFromRight = len(nums) - min(maxElem[1], minElem[1])
        endOne = (len(nums) - maxElem[1]) + (minElem[1] + 1)
        endTwo = (len(nums) - minElem[1]) + (maxElem[1] + 1)

        return min(removeFromleft, removeFromRight, endOne, endTwo)