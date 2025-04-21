class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # https://claude.site/artifacts/4ad470f8-0678-4910-b480-7d606a8cb366
        min_val = max_val = cur = 0 

        for d in differences: 
            #Difference array concept
            cur += d 
            max_val = max(cur, max_val)
            min_val = min(cur, min_val)

            if max_val - min_val > upper - lower: 
                return 0 

        return (upper - lower) - (max_val - min_val) + 1