class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        ans = -1
        while l <= r: 
            mid = (l + r) // 2 
            if target <= nums[mid]: 
                r = mid - 1
                ans = mid
            else: 
                l = mid + 1

        return ans if ans != -1 else len(nums)

        