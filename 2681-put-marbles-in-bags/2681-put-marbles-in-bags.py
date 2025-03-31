class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        n = len(weights)
        #Intuition is that we always include the first and last of an subarray, 
        #So pair for that, for each case and the most max pair sum and min pair sum 
        #Then just difference it 
        pairWeights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pairWeights.sort()
        max_pair_sum = sum(pairWeights[-(k - 1):])
        min_pair_sum = sum(pairWeights[:(k - 1)])

        return max_pair_sum - min_pair_sum