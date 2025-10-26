class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = len(nums) - 1 
        left = -1 
        right = -1
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] <= target: 
                l = mid + 1
                if nums[mid] == target: 
                    right = mid 
            else:
                r = mid - 1

        l = 0 
        r = len(nums) - 1 
        while l <= r: 
            mid = (l + r) // 2
            if target <= nums[mid]: 
                r = mid - 1
                if nums[mid] == target: 
                    left = mid 
            else:
                l = mid + 1

        return [left, right]
        

        

