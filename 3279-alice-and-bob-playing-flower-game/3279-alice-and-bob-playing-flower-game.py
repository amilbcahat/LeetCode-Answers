class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        oddCOne = 0 
        evenCOne = 0 
        oddCTwo = 0
        evenCTwo = 0
        for i in range(1, n + 1): 
            if i & 1: 
                oddCOne += 1
            else: 
                evenCOne += 1

        for i in range(1, m + 1): 
            if i & 1: 
                oddCTwo += 1
            else: 
                evenCTwo += 1

        return oddCOne * evenCTwo + oddCTwo * evenCOne       