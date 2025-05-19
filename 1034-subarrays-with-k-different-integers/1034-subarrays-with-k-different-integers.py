class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Array to count distinct values in the current window
        count = [0] * (len(nums) + 1)
        result = 0  # Total number of subarrays with exactly k distinct integers
        left = 0  # Left boundary of the window
        right = 0  # Right boundary of the window
        windowCount = 0  # Current number of valid subarrays in the window

        while right < len(nums):
            # Increase the count for the current element and move the right boundary
            if count[nums[right]] == 0:
                k -= 1
            count[nums[right]] += 1
            right += 1

            # If there are more than k distinct elements, adjust the window from the left
            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1
                windowCount = 0

            # If there are exactly k distinct elements, count the subarrays
            if k == 0:
                # Move the left boundary to reduce the window size while maintaining k distinct elements
                while count[nums[left]] > 1:
                    count[nums[left]] -= 1
                    left += 1
                    windowCount += 1
                # Add the current number of valid subarrays to the result
                result += (windowCount + 1)

        return result


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