class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            rob1 , rob2 = 0, 0 
            #[rob1, rob2 , n , n+1 , n+2]
        
            for n in arr:
                temp = max(n+rob1 ,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2  
        #Just avoid take last and first element together ! 
        #Added nums[0] here to take care of the edge case of array of size 1 
        #[We can either include last element or first element here ]
        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))
