class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        minElem = nums[0]
        maxElem = nums[-1]
        half = len(nums) // 2

        deletions = 0 
        removeFromleft = max(maxElem[1] + 1, minElem[1] + 1)
        removeFromRight = len(nums) - min(maxElem[1], minElem[1])
        endOne = (len(nums) - maxElem[1]) + (minElem[1] + 1)
        endTwo = (len(nums) - minElem[1]) + (maxElem[1] + 1)

        return min(removeFromleft, removeFromRight, endOne, endTwo)