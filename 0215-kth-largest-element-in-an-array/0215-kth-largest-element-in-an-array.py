class Solution:
    # def partition(self,nums,left,right):
        
    #     pivot , p = nums[right] , left 
    #     for i in range(left,right):
    #         if nums[i] <= pivot : 
    #             nums[p] , nums[i] = nums[i] , nums[p]
    #             p+=1
    #     nums[p], nums[right] = nums[right], nums[p]
    #     return p


    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Counting Sort -> 
        maxValue = max(nums)
        minValue = min(nums)
        count = [0] * ((maxValue - minValue) + 1)
        for num in nums: 
            count[num - minValue] += 1

        for i in range(len(count) - 1, -1, -1): 
            k -= count[i]
            if k <= 0: 
                return i + minValue

        return -1

        #New implementation check editorial (Hoare's to tackle duplicates) -> 
        # def quickselect(nums, k): 
        #     pivot = random.choice(nums)
        #     left, right, mid = [], [], []
        #     for num in nums: 
        #         if num > pivot: 
        #             left.append(num)
        #         elif num < pivot: 
        #             right.append(num)
        #         else: 
        #             mid.append(num)

        #     if k <= len(left): 
        #         return quickselect(left, k)
            
        #     if len(left) + len(mid) < k: 
        #         return quickselect(right, k - len(left) - len(mid))

        #     return pivot

        # return quickselect(nums, k)


        # Does not pass now
        # k = len(nums)-k 
        # left , right = 0 , len(nums)-1 

        # while left < right : 
        #     pivot = self.partition(nums,left,right)

        #     if pivot < k : 
        #         left = pivot + 1 
        #     elif pivot > k : 
        #         right = pivot -1 
        #     else : 
        #         break 
        # return nums[k]  
