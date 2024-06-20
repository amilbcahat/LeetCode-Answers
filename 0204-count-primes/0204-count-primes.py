class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2 : 
            return 0 

        isPrime = [True] * n 
        isPrime[0] = isPrime[1] = False 

        for i in range(1 , int(n ** 0.5) + 1): 
            if (isPrime[i]):
                for multi_of_i in range(i * i , n , i):
                    isPrime[multi_of_i] = False 
        
        return sum(isPrime)
        