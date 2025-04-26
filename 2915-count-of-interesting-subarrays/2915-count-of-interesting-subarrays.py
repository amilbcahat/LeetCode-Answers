from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # ==========================================================================
        # Mathematical foundation for this solution:
        # ==========================================================================
        # Let prefix[i] = count of elements from index 0 to i where nums[i] % modulo == k
        # 
        # For a subarray from index j to index i to be "interesting":
        # (prefix[i] - prefix[j-1]) % modulo = k
        # 
        # To find all valid previous positions j-1:
        # (prefix[i] - prefix[j-1]) % modulo = k
        # 
        # Rearranging:
        # prefix[i] - prefix[j-1] = k + n*modulo   (for some integer n)
        # prefix[j-1] = prefix[i] - k - n*modulo
        # 
        # Taking modulo of both sides:
        # prefix[j-1] % modulo = (prefix[i] - k - n*modulo) % modulo
        #                       = (prefix[i] - k) % modulo   (since n*modulo % modulo = 0)
        # 
        # To ensure non-negative result in modular arithmetic:
        # prefix[j-1] % modulo = (prefix[i] + modulo - k) % modulo
        # 
        # This is our target value to look for in the prefix map
        # ==========================================================================
        
        # Hash map to track frequency of prefix sums modulo 'modulo'
        # Initialize with {0:1} for empty subarray (or before the first element)
        preMap = defaultdict(int)
        preMap[0] = 1
        
        # Running count of elements that satisfy nums[i] % modulo == k
        prefix = 0
        
        # Result counter for interesting subarrays
        res = 0
        
        # Process each element in the array
        for n in nums:
            # Update prefix count if current number satisfies the condition
            if n % modulo == k:
                prefix += 1
            
            # Calculate target remainder for previous positions
            # This is the key insight: what remainder should previous positions have
            # to make this current position complete an interesting subarray?
            target = (prefix + modulo - k) % modulo
            
            # Add count of previous positions that form interesting subarrays
            # with current position
            res += preMap[target]
            
            # Update the frequency map with current prefix's remainder
            preMap[prefix % modulo] += 1
            
        return res

        # ==========================================================================
        # Example calculation with nums = [3,1,9,6], modulo = 3, k = 0:
        # ==========================================================================
        # Initial state: preMap = {0:1}, prefix = 0, res = 0
        # 
        # Element 3 (index 0):
        #   3 % 3 = 0, so prefix = 1
        #   target = (1 + 3 - 0) % 3 = 4 % 3 = 1
        #   res += preMap[1] = 0  (no previous positions with remainder 1)
        #   update preMap[1] += 1, so preMap = {0:1, 1:1}
        # 
        # Element 1 (index 1):
        #   1 % 3 ≠ 0, so prefix remains 1
        #   target = (1 + 3 - 0) % 3 = 4 % 3 = 1
        #   res += preMap[1] = 1  (one previous position with remainder 1)
        #   update preMap[1] += 1, so preMap = {0:1, 1:2}
        # 
        # Element 9 (index 2):
        #   9 % 3 = 0, so prefix = 2
        #   target = (2 + 3 - 0) % 3 = 5 % 3 = 2
        #   res += preMap[2] = 0  (no previous positions with remainder 2)
        #   update preMap[2] += 1, so preMap = {0:1, 1:2, 2:1}
        # 
        # Element 6 (index 3):
        #   6 % 3 = 0, so prefix = 3
        #   target = (3 + 3 - 0) % 3 = 6 % 3 = 0
        #   res += preMap[0] = 1  (one previous position with remainder 0)
        #   update preMap[0] += 1, so preMap = {0:2, 1:2, 2:1}
        # 
        # Final result: res = 2
        # ==========================================================================