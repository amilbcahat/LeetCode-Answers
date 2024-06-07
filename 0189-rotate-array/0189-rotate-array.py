class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #Also do Shift 2D , to understand this concept really well 
        if k == 0 : 
            return 

        arr = nums.copy()
        for i in range(len(nums) - 1 , -1 , -1 ): 
            targetIndex = (i - k) % len(nums)
            nums[i] = arr[targetIndex]

        return nums
