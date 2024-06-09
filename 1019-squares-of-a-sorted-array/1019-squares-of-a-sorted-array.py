class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Intuition is that since its sorted the biggest values will be either at the both ends

        l , r = 0 , len(nums) - 1
        res = []

        while l <= r : 
            if nums[l] ** 2 > nums[r] ** 2 : 
                res.append(nums[l] ** 2)
                l += 1 
            else :
                res.append(nums[r] ** 2)
                r -= 1 

        return res[::-1]