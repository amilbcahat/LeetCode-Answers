class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l , r = 0 , len(nums)-1 
        i = 0 
        def swap(i, j): 
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
       #We use two pointers l and r , l moves when we find a 0 and it is swapped with left array hence maintaining a number 0f zeroes in start 
       #r is used to keep track of last element of 2's and is moved when i finds a 2 and is swapped 
       #But we dont increment i , incase we find a 2 , because then it messes up the 0 order 
       #Since 0 and 2 are sorted , 1 automatically resides in the middle ! 

        while i <= r: 
            if nums[i] == 0: 
                swap(l, i)
                l += 1 
            if nums[i] == 2:
                swap(i, r)
                r -= 1
                #I is decremented to cancel out the increment outside , and so displacement is 0 of i , we increment it outside , because then while loop can go in a state , infinite loop
                i -= 1
            i += 1