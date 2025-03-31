from math import sqrt
from heapq import heapify, heappop
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Intuition: 
        # Phase 1: Calculate the prime scores for each number
        N = len(nums)
        prime_scores = []
        res = 1
        MOD = 10 ** 9 + 7
        
        for n in nums: 
            score = 0
            # Find all prime factors of n
            for f in range(2, int(sqrt(n)) + 1): 
                if n % f == 0: 
                    # Increment score for each unique prime factor
                    score += 1
                    # Remove all occurrences of this factor
                    while n % f == 0: 
                        n = n // f 
            # If n > 1, it's a prime number itself
            if n >= 2:
                score += 1
            prime_scores.append(score)

        # Phase 2: Use Monotonic Stack to find boundaries
        # For each element, find the region where it has the highest prime score
        stack = []
        left_bound = [-1] * N  # Index of previous element with higher prime score
        right_bound = [N] * N  # Index of next element with higher prime score

        for i, s in enumerate(prime_scores): 
            # Pop elements with lower prime scores (current element dominates them)
            while stack and prime_scores[stack[-1]] < s: 
                indx = stack.pop()
                right_bound[indx] = i  # Current element is their right boundary
            
            # Current element's left boundary is the top of stack (if exists)
            if stack: 
                left_bound[i] = stack[-1]
            
            stack.append(i)

        # Phase 3: Greedily pick elements with highest values first
        # Create max heap of (-value, index) pairs to process largest values first
        max_heap = [(-n, i) for i, n in enumerate(nums)]
        heapify(max_heap)
        
        # Process elements in order of decreasing value
        while k > 0: 
            n, i = heappop(max_heap)
            n = -n  # Convert back to positive value
            
            # Calculate number of subarrays where this element has highest prime score
            right_sub = right_bound[i] - i  # Number of valid right boundaries
            left_sub = i - left_bound[i]    # Number of valid left boundaries
            cnt = right_sub * left_sub      # Total number of subarrays
            
            # Determine how many operations to perform with this element
            operations = min(k, cnt)
            
            # Update result by multiplying by this element 'operations' times
            res = (res * pow(n, operations, MOD)) % MOD
            
            # Reduce remaining operations
            k -= operations
            
        return res