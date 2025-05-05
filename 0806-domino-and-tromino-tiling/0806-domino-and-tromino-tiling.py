class Solution:
    def numTilings(self, n: int) -> int:
        first = 1 
        second = 2
        third = 5
        mod = 10 ** 9 + 7
        arr = [first, second, third]

        if n >= 4: 
            cur = -1
            for i in range(4, n + 1): 
                cur = third * 2 + first
                first = second 
                second = third 
                third = cur 

        return arr[n - 1] if n <= 3 else cur % mod