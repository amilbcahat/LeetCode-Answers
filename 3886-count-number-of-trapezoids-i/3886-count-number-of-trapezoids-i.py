from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7 
        groupSlopes = defaultdict(int)
        for x, y in points: 
            groupSlopes[y] += 1
        
        res = total = 0
        for y, count in groupSlopes.items(): 
            lines = count * (count - 1) // 2 #ways of choosing two points 
            res = (res + total * lines) % MOD 
            total = (total + lines) % MOD  
        
        return res


# Great question! Let me break down the mathematical formula step by step to show how total and res fit in.
# The Core Formula We Want to Compute
# For trapezoids, we want:
# Total Trapezoids = C(n₁,2)×C(n₂,2) + C(n₁,2)×C(n₃,2) + C(n₁,2)×C(n₄,2) + 
#                    C(n₂,2)×C(n₃,2) + C(n₂,2)×C(n₄,2) + 
#                    C(n₃,2)×C(n₄,2) + ...
# Rearranging the Formula
# We can factor this as:
# = C(n₁,2) × [C(n₂,2) + C(n₃,2) + C(n₄,2) + ...] +
#   C(n₂,2) × [C(n₃,2) + C(n₄,2) + ...] +
#   C(n₃,2) × [C(n₄,2) + ...] + 
#   ...
# How the Algorithm Maps to This
# Let's trace through with levels having [3, 4, 2] points:
# Step 1: Process level 1 (3 points)
# pairs₁ = C(3,2) = 3
# total = 0        (sum of previous pairs)
# res = 0 + (0 × 3) = 0    (no previous levels to multiply with)
# total = 0 + 3 = 3        (update total for next iteration)
# Step 2: Process level 2 (4 points)
# pairs₂ = C(4,2) = 6
# total = 3        (sum of previous pairs = C(3,2))
# res = 0 + (3 × 6) = 18   (this adds C(3,2) × C(4,2))
# total = 3 + 6 = 9        (update total = C(3,2) + C(4,2))
# Step 3: Process level 3 (2 points)
# pairs₃ = C(2,2) = 1
# total = 9        (sum of previous pairs = C(3,2) + C(4,2))
# res = 18 + (9 × 1) = 27  (this adds [C(3,2) + C(4,2)] × C(2,2))
# total = 9 + 1 = 10       (update total for potential next iteration)
# Verification
# Let's verify: 27 = C(3,2)×C(4,2) + C(3,2)×C(2,2) + C(4,2)×C(2,2)
# = 3×6 + 3×1 + 6×1
# = 18 + 3 + 6
# = 27 ✓
# The Key Insight

# total = Running sum of all previous levels' pair counts

# At step i, total = C(n₁,2) + C(n₂,2) + ... + C(nᵢ₋₁,2)


# res = Running sum of the actual answer

# At step i, we add total × pairs_i which gives us all combinations of current level with all previous levels



# The algorithm cleverly processes levels one by one, and at each step, multiplies the current level's pairs with the sum of ALL previous levels' pairs - which is exactly what the rearranged formula does!