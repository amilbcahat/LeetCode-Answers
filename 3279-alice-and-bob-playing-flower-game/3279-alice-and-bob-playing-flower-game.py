class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m * n) // 2 #check editorial for this
        # ans = 0
        # oddCOne = 0 
        # evenCOne = 0 
        # oddCTwo = 0
        # evenCTwo = 0

        # #Alice would win when x + y is odd :)
        # for i in range(1, n + 1): 
        #     if i & 1: 
        #         oddCOne += 1
        #     else:                           
        #         evenCOne += 1

        # for i in range(1, m + 1): 
        #     if i & 1: 
        #         oddCTwo += 1                        
        #     else: 
        #         evenCTwo += 1

        # return oddCOne * evenCTwo + oddCTwo * evenCOne       