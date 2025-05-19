class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #One Pass 
        count = defaultdict(int)
        total = 0 
        left = 0 
        right = 0 
        currentWin = 0

        while right < len(nums): 
            if count[nums[right]] == 0: 
                k -= 1
            
            count[nums[right]] += 1
            right += 1

            if k < 0: 
                count[nums[left]] -= 1
                if count[nums[left]] == 0: 
                    k += 1
                left += 1
                currentWin = 0

            if k == 0: 
                while count[nums[left]] > 1: 
                    count[nums[left]] -= 1
                    left += 1
                    currentWin += 1

                total += (currentWin + 1)

        return total


        #Two Pass         
        # def atmost(k): 
        #     l = 0 
        #     res = 0 
        #     distinct = set()
        #     countMap = defaultdict(int)

        #     for r in range(len(nums)):
        #         distinct.add(nums[r])
        #         countMap[nums[r]] += 1 

        #         while l <= r and len(distinct) > k : 
        #             countMap[nums[l]] -= 1 
        #             if countMap[nums[l]] == 0 : 
        #                 distinct.remove(nums[l])
        #             l += 1

        #         res += (r - l + 1)

        #     return res 

        # return atmost(k) - atmost(k - 1)