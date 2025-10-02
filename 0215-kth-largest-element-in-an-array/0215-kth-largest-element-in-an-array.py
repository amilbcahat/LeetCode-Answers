class Solution:
    def partition(self,nums,left,right):
        
        pivot , p = nums[right] , left 
        for i in range(left,right):
            if nums[i] <= pivot : 
                nums[p] , nums[i] = nums[i] , nums[p]
                p+=1
        nums[p], nums[right] = nums[right], nums[p]
        return p


    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k 
        left , right = 0 , len(nums)-1 

        while left < right : 
            pivot = self.partition(nums,left,right)

            if pivot < k : 
                left = pivot + 1 
            elif pivot > k : 
                right = pivot -1 
            else : 
                break 
        return nums[k]  
