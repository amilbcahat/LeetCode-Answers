class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElem = max(nums)
        #Solve generally for atmost , and then calculate for the needed solution !
        l = 0 
        count = 0 
        res = 0
        n = len(nums)

        #Count for less than k 

        for r in range(len(nums)):
            count += 1 if nums[r] == maxElem else 0 
            #Notice that here it is k - 1 (k not included)
            while l <= r and count > k - 1: 
                count -= 1 if nums[l] == maxElem else 0 
                l += 1 

            # print(nums[l : r + 1])
            res += (r - l + 1)

        # print(res)

        #Now we calculate for atmost k , by no.of subarrays - atmost k - 1
        return (n * (n + 1) // 2) - res 

            

             