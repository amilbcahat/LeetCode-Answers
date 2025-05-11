class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #Check Editorial, apt explanation
        sum1 = sum2 = 0 
        zero1 = zero2 = 0 

        for n in nums1: 
            sum1 += n
            if n == 0: 
                zero1 += 1
                sum1 += 1

        for n in nums2: 
            sum2 += n
            if n == 0: 
                zero2 += 1
                sum2 += 1

        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2): 
            return -1 

        return max(sum1, sum2)