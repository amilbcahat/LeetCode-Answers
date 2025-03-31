class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prime_scores = []
        res = 1
        MOD = 10 ** 9 + 7
        for n in nums: 
            score = 0
            for f in range(2, int(sqrt(n)) + 1): 
                if n % f == 0: 
                    score += 1
                    while n % f == 0: 
                        n = n // f 
            if n >= 2:
                score += 1
            prime_scores.append(score)

        stack = []
        left_bound = [-1] * N 
        right_bound = [N] * N

        for i, s in enumerate(prime_scores): 
            while stack and prime_scores[stack[-1]] < s: 
                indx = stack.pop()
                right_bound[indx] = i
            if stack: 
                left_bound[i] = stack[-1]
            stack.append(i)

        max_heap = [(-n, i) for i, n in enumerate(nums)]
        heapify(max_heap)
        while k > 0: 
            n, i = heapq.heappop(max_heap)
            n = -n 
            right_sub = right_bound[i] - i 
            left_sub = i - left_bound[i] 
            cnt = right_sub * left_sub 
            operations = min(k, cnt)
            res = (res * pow(n, operations, MOD)) % MOD
            k -= operations
        return res