class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for s in spells: 
            l = 0 
            r = len(potions) - 1 
            ans = len(potions)
            while l <= r: 
                mid = (l + r) // 2
                val = potions[mid] * s

                if val >= success: 
                    r = mid - 1
                    ans = mid 
                else: 
                    l = mid + 1 

            res.append(len(potions) - ans)

        return res