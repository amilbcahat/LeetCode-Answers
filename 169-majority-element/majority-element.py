class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #Boyer - Moore Algorithm 
        #BAsically , we cancel out the frequencies , by going through the array
        #And get the element with majority 
        res , count = 0 , 0 

        for n in nums : 
            #If count of a specific element goes 0 , then change the element as it will introduce 
            #the possibility of a better ans 
            if count == 0 :
                res = n 
            
            #Increment if found a match with currently assument ans , else decrement 
            count += (1 if n == res else -1)

        return res 