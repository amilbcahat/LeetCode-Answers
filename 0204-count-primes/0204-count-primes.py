class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2 : 
            return 0 

        isPrime = [True] * n 
        isPrime[0] = isPrime[1] = False 

        for i in range(2 , int(n ** 0.5) + 1): 

            for multi in range(i * i , n , i):
                if isPrime[i] : 
                    isPrime[multi] = False 

        return sum(isPrime)