class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Just one Binary search
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            #Did we find the target ? 
            if nums[mid] == target: 
                return mid

            #left is sorted, check if target is present 
            elif nums[l] <= nums[mid]: 
                if nums[l] <= target < nums[mid]: 
                    #target is here find it
                    r = mid - 1
                else: 
                    #not here go to right sub
                    l = mid + 1

            #if not then right would be sorted
            else:
                if nums[mid] < target <= nums[r]: 
                    #target is here , find now
                    l = mid + 1
                else: 
                    #not here, go to left sub
                    r = mid - 1

        return -1
                 
        #One solution is simply shifting the indicies
        # pivot = 0

        # def check(arr, mid): 
        #     if arr[0] > arr[mid]: 
        #         return True 
        #     return False 

        # l = 0 
        # r = len(nums) - 1
        # while l <= r: 
        #     mid = (l + r) // 2
        #     if check(nums, mid): 
        #         r = mid - 1
        #         pivot = mid
        #     else: 
        #         l = mid + 1

        # l = 0 
        # r = len(nums) - 1

        # print(pivot)
        # while l <= r: 
        #     mid = (l + r) // 2
        #     shift_idx = (mid + pivot) % len(nums)
        #     if nums[shift_idx] == target: 
        #         return shift_idx
        #     elif nums[shift_idx] < target:
        #         l = mid + 1
        #     else: 
        #         r = mid - 1

        # return -1


        #Solve based on pivot
        # pivot = 0

        # def check(arr, mid): 
        #     if arr[0] > arr[mid]: 
        #         return True 
        #     return False 

        # l = 0 
        # r = len(nums) - 1
        # while l <= r: 
        #     mid = (l + r) // 2
        #     if check(nums, mid): 
        #         r = mid - 1
        #         pivot = mid
        #     else: 
        #         l = mid + 1

        # if nums[pivot] <= target <= nums[len(nums) - 1]: 
        #     l = pivot 
        #     r = len(nums) - 1
        #     while l <= r: 
        #         mid = (l + r) // 2
        #         if nums[mid] == target: 
        #             return mid
        #         elif target <= nums[mid]: 
        #             r = mid - 1
        #         else: 
        #             l = mid + 1
        # else: 
        #     l = 0 
        #     r = pivot - 1
        #     while l <= r: 
        #         mid = (l + r) // 2
        #         if nums[mid] == target: 
        #             return mid
        #         elif target <= nums[mid]: 
        #             r = mid - 1
        #         else: 
        #             l = mid + 1

        # return -1
