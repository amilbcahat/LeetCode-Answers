class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0

        def check(arr, mid): 
            if arr[0] > arr[mid]: 
                return True 
            return False 

        l = 0 
        r = len(nums) - 1
        while l <= r: 
            mid = (l + r) // 2
            if check(nums, mid): 
                r = mid - 1
                pivot = mid
            else: 
                l = mid + 1

        if nums[pivot] <= target <= nums[len(nums) - 1]: 
            l = pivot 
            r = len(nums) - 1
            while l <= r: 
                mid = (l + r) // 2
                if nums[mid] == target: 
                    return mid
                elif target <= nums[mid]: 
                    r = mid - 1
                else: 
                    l = mid + 1
        else: 
            l = 0 
            r = pivot - 1
            while l <= r: 
                mid = (l + r) // 2
                if nums[mid] == target: 
                    return mid
                elif target <= nums[mid]: 
                    r = mid - 1
                else: 
                    l = mid + 1

        return -1
