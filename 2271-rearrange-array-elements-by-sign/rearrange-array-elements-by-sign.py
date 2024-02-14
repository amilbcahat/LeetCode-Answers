class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for n in nums :
            if n > 0 : 
                pos.append(n)
            else : 
                neg.append(n)
        p  , n = 0 ,0
        for i in range(len(nums)):
            if i % 2 == 0 : 
                #pos first 
                nums[i] = pos[p]
                p+= 1 
            else : 
                nums[i] = neg[n]
                n += 1
        #
        return nums