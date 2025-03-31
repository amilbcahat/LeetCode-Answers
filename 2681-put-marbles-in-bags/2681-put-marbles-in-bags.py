class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        n = len(weights)
        #Intuition is that we always include the first and last of an subarray, 
        #So pair for that, for each case and the most max pair sum and min pair sum 
        #Then just difference it 
        pairWeights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        print(pairWeights)
        pairWeights.sort()
        max_pair_sum = sum(pairWeights[-(k - 1):])
        print(pairWeights[-(k - 1):])
        min_pair_sum = sum(pairWeights[:(k - 1)])
        print(pairWeights[:(k - 1)])
        return max_pair_sum - min_pair_sum

#         Understanding the Marble Bags Problem
# Let me walk through this with a clear example and mathematical proof side by side.
# Example: [1, 3, 5, 1] and k=2 bags
# Step 1: Explore All Possible Splits
# We have 3 ways to split:

# Split after position 0: [1] | [3, 5, 1]

# First bag cost: 1+1 = 2
# Second bag cost: 3+1 = 4
# Total: 6


# Split after position 1: [1, 3] | [5, 1]

# First bag cost: 1+3 = 4
# Second bag cost: 5+1 = 6
# Total: 10


# Split after position 2: [1, 3, 5] | [1]

# First bag cost: 1+5 = 6
# Second bag cost: 1+1 = 2
# Total: 8



# Maximum cost = 10, Minimum cost = 6, Difference = 4
# Mathematical Explanation
# For any split into k bags, the total cost can be written as:
# CopyTotalCost = w₀ + wₙ₋₁ + Sum of all (wᵢ + wᵢ₊₁) at split points
# In our example:

# w₀ = 1 (first marble in array)
# wₙ₋₁ = 1 (last marble in array)

# For each split:

# Split after position 0: Adds (w₀ + w₁) = (1 + 3) = 4
# Split after position 1: Adds (w₁ + w₂) = (3 + 5) = 8
# Split after position 2: Adds (w₂ + w₃) = (5 + 1) = 6

# Let's verify that our formula works:

# Split after position 0: 1 + 1 + 4 = 6 ✓
# Split after position 1: 1 + 1 + 8 = 10 ✓
# Split after position 2: 1 + 1 + 6 = 8 ✓

# Key Insight
# Since w₀ and wₙ₋₁ are included in every arrangement, when we calculate the difference between max and min costs, they cancel out:
# CopyMaxCost - MinCost = (w₀ + wₙ₋₁ + MaxSplitSum) - (w₀ + wₙ₋₁ + MinSplitSum)
#                    = MaxSplitSum - MinSplitSum
# In our example:

# MaxSplitSum = 8 (split after position 1)
# MinSplitSum = 4 (split after position 0)
# MaxCost - MinCost = 8 - 4 = 4

# This is why sorting the adjacent pair sums and taking the difference between the largest k-1 and smallest k-1 pair sums gives us the exact answer.