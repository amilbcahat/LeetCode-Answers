class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #https://leetcode.com/problems/subarrays-with-k-different-integers/description/ <- Same as 

        k = len(set(nums))
        def atmost(k): 
            l = 0
            res = 0 
            distinct = set()
            countMap = defaultdict(int)
            for r in range(len(nums)): 
                distinct.add(nums[r])
                countMap[nums[r]] +=1 

                while l <= r and len(distinct) > k: 

                    countMap[nums[l]] -= 1
                    if countMap[nums[l]] == 0: 
                        distinct.remove(nums[l])
                    l += 1

                res += (r - l + 1)

            return res

        return atmost(k) - atmost(k - 1)