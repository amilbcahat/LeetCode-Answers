class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1 
        res = nums[0]

        while l <= r :
            #Array is already sorted  
            if nums[l] < nums[r]:
                res = min(res , nums[l])
                break 

            mid = (l + r) // 2 
            res = min(res , nums[mid])
            if nums[mid] >= nums[l]:
                #We are in left side 
                #We want to move to right side to get smaller values 
                l = mid + 1 
            else : 
                #If we are in right side 
                #We want to move left , to find smaller values in right side itself ! 
                r = mid - 1 

        return res 