class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def get_primes(limit: int) -> List[int]:
            is_prime = [True] * (limit + 1)
            primes = []
            # Start marking from the first prime number (2)
            for number in range(2, limit + 1):
                if not is_prime[number]:
                    continue

                # Store the prime number
                primes.append(number)

                # Mark multiples of the prime number as non-prime
                for multiple in range(number * number, limit + 1, number):
                    is_prime[multiple] = False

            return primes

        def _pow(x, n): 
            if x == 0: 
                return 0
            if n == 0: 
                return 1 
            res = _pow(x, n // 2)
            res = (res * res) % MOD
            return (x * res) % MOD if n % 2 else res

        # Intuition: 
        # Phase 1: Calculate the prime scores for each number
        N = len(nums)
        prime_scores = []
        res = 1
        MOD = 10 ** 9 + 7
        maxElem = max(nums)
        primes = get_primes(maxElem)

        for n in nums: 
            score = 0
            # Find all prime factors of n
            for prime in primes: 
                if prime * prime > n: 
                    break 
                if n % prime != 0: 
                    continue 
                score += 1
                    # Remove all occurrences of this factor
                while n % prime == 0: 
                    n = n // prime
            # If n > 1, it's a prime number itself
            if n >= 2:
                score += 1
            prime_scores.append(score)

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

        sorted_array = sorted([(nums[i], i) for i in range(len(nums))], reverse=True)
        indx = 0
        while k > 0 and indx < N: 
            n, i = sorted_array[indx]
            # Calculate number of subarrays where this element has highest prime score
            right_sub = right_bound[i] - i  # Number of valid right boundaries
            left_sub = i - left_bound[i]    # Number of valid left boundaries
            cnt = right_sub * left_sub      # Total number of subarrays
            
            # Determine how many operations to perform with this element
            operations = min(k, cnt)
            
            # Update result by multiplying by this element 'operations' times
            res = (res * _pow(n, operations)) % MOD
            # Reduce remaining operations
            k -= operations
            indx += 1

        return res 



        #Less Optimal 
        # for n in nums: 
        #     score = 0
        #     # Find all prime factors of n
        #     for f in range(2, int(sqrt(n)) + 1): 
        #         if n % f == 0: 
        #             # Increment score for each unique prime factor
        #             score += 1
        #             # Remove all occurrences of this factor
        #             while n % f == 0: 
        #                 n = n // f 
        #     # If n > 1, it's a prime number itself
        #     if n >= 2:
        #         score += 1
        #     prime_scores.append(score)

        # # Phase 2: Use Monotonic Stack to find boundaries
        # # For each element, find the region where it has the highest prime score
        # stack = []
        # left_bound = [-1] * N  # Index of previous element with higher prime score
        # right_bound = [N] * N  # Index of next element with higher prime score

        # for i, s in enumerate(prime_scores): 
        #     # Pop elements with lower prime scores (current element dominates them)
        #     while stack and prime_scores[stack[-1]] < s: 
        #         indx = stack.pop()
        #         right_bound[indx] = i  # Current element is their right boundary
            
        #     # Current element's left boundary is the top of stack (if exists)
        #     if stack: 
        #         left_bound[i] = stack[-1]
            
        #     stack.append(i)

        # # Phase 3: Greedily pick elements with highest values first
        # # Create max heap of (-value, index) pairs to process largest values first
        # max_heap = [(-n, i) for i, n in enumerate(nums)]
        # heapify(max_heap)
        
        # # Process elements in order of decreasing value
        # while k > 0: 
        #     n, i = heappop(max_heap)
        #     n = -n  # Convert back to positive value
            
        #     # Calculate number of subarrays where this element has highest prime score
        #     right_sub = right_bound[i] - i  # Number of valid right boundaries
        #     left_sub = i - left_bound[i]    # Number of valid left boundaries
        #     cnt = right_sub * left_sub      # Total number of subarrays
            
        #     # Determine how many operations to perform with this element
        #     operations = min(k, cnt)
            
        #     # Update result by multiplying by this element 'operations' times
        #     res = (res * pow(n, operations, MOD)) % MOD
            
        #     # Reduce remaining operations
        #     k -= operations

        return res