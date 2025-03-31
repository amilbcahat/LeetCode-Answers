class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Sieve of Eratosthenes to efficiently find all prime numbers up to a limit
        def get_primes(limit: int) -> List[int]:
            is_prime = [True] * (limit + 1)
            primes = []
            # Start marking from the first prime number (2)
            for number in range(2, limit + 1):
                if not is_prime[number]:
                    continue
                
                # Store the prime number
                primes.append(number)
                
                # Mark multiples of the prime number as non-prime (optimization: start from number^2)
                for multiple in range(number * number, limit + 1, number):
                    is_prime[multiple] = False
            
            return primes
        
        # Efficient binary exponentiation algorithm with modular arithmetic
        def _pow(x, n):
            # Base cases
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            # Recursive case: compute x^(n/2) first
            res = _pow(x, n // 2)
            # Square the result and apply modulo
            res = (res * res) % MOD
            # If n is odd, multiply by x one more time
            return (x * res) % MOD if n % 2 else res
        
        # Initialize variables
        N = len(nums)
        prime_scores = []  # Will store the prime score of each number
        res = 1  # Initial result value
        MOD = 10 ** 9 + 7  # Modulo to prevent overflow
        
        # Find the maximum element to limit our prime search
        maxElem = max(nums)
        # Get all primes up to maxElem using Sieve of Eratosthenes
        primes = get_primes(maxElem)
        
        # Phase 1: Calculate the prime scores for each number
        for n in nums:
            score = 0
            # Find all prime factors of n
            for prime in primes:
                # Optimization: if prime^2 > n, no more prime divisors are possible
                if prime * prime > n:
                    break
                # Skip primes that don't divide n
                if n % prime != 0:
                    continue
                
                # Found a prime factor, increment score by 1 (we only count distinct prime factors)
                score += 1
                
                # Remove all occurrences of this prime factor from n
                while n % prime == 0:
                    n = n // prime
            
            # If n > 1 after all checks, n itself is a prime
            if n >= 2:
                score += 1
                
            prime_scores.append(score)
        
        # Phase 2: Use Monotonic Stack to find boundaries for each element
        stack = []
        left_bound = [-1] * N  # Index of previous element with higher prime score
        right_bound = [N] * N  # Index of next element with higher prime score
        
        for i, s in enumerate(prime_scores):
            # Pop elements with lower prime scores from the stack
            # Current element (i) becomes their right boundary
            while stack and prime_scores[stack[-1]] < s:
                indx = stack.pop()
                right_bound[indx] = i
            
            # If stack is not empty, the top element is the left boundary for current element
            if stack:
                left_bound[i] = stack[-1]
            
            # Add current element to stack
            stack.append(i)
        
        # Phase 3: Process elements in descending order of value
        # Sort (value, index) pairs in descending order of value
        sorted_array = sorted([(nums[i], i) for i in range(len(nums))], reverse=True)
        indx = 0
        
        # Process elements until we've used all k operations
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

        # return res