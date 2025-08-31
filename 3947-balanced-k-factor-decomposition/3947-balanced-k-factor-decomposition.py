class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        factors = defaultdict(list)
        mostMin = float("inf")
        def backtrack(cur, n, k): 
            nonlocal mostMin
            if k == 0: 
                if n == 1: 
                    arr = cur.copy()
                    prof = max(arr) - min(arr)
                    mostMin = min(prof, mostMin)
                    factors[prof] = arr 
                return

            for i in range(1, n + 1): 
                if n % i == 0: 
                    backtrack(cur + [i], n // i, k - 1)

        backtrack([], n, k)

        print(factors)
        return factors[mostMin]