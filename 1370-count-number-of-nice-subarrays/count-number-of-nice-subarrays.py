class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        #Atmost sliding window algo !
        def atmostOdd(k):
            l = 0 

            res = 0 
            countOdd = 0 
            for r in range(len(nums)):
                countOdd += 1 if nums[r] % 2 != 0 else 0 
                while l <= r and countOdd > k :
                    countOdd -= 1 if nums[l] % 2 != 0 else 0 
                    l += 1

                # print(nums[l : r + 1])

                res += (r - l + 1)

            return res 

        #Subarray with K odds = Subarray with atmost K odds - Subarray with K - 1 odds 
        return (atmostOdd(k) - atmostOdd(k - 1))

        
