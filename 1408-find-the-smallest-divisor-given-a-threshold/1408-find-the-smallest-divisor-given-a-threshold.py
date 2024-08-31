class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def possible(curDiv):
            #Calculate sum 
            total = 0  
            for n in nums : 
                total += (math.ceil(n / curDiv))

            return total <= threshold 

        l = 1 
        r = max(nums)
        #Range of Divisors 
        res = float("inf")
        while l <= r : 
            #Find correct one with Binary Search 
            curDiv = (l + r) // 2 
            if possible(curDiv) :
                res = min(res , curDiv) 
                r = curDiv - 1 
            else: 
                l = curDiv + 1 

        return -1 if res == float("inf") else res 
