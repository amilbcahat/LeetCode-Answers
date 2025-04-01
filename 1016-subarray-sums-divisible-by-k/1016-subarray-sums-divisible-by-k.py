class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Initialize a defaultdict to track frequency of remainders
        # Default value is 0 for any new key
        preMap = defaultdict(int)
        
        # Initialize with remainder 0 having count 1
        # This handles the case where a prefix sum itself is divisible by k
        preMap[0] = 1
        
        # Track the running sum and result count
        curSum = 0
        res = 0
        
        # Formula: If prefixSum[j] % k = prefixSum[i] % k, then (prefixSum[j] - prefixSum[i]) % k = 0
        # This means the subarray from index i+1 to j has a sum divisible by k
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Update running sum with current element
            curSum += num
            
            # Calculate the remainder when current sum is divided by k
            remain = curSum % k
            
            # If we've seen this remainder before, it means:
            # For some previous index i where prefixSum[i] % k = remain,
            # The subarray from i+1 to current index has sum divisible by k
            res += preMap[remain]
            
            # Increment the count of current remainder for future calculations
            preMap[remain] += 1
        
        # Return the total count of subarrays divisible by k
        return res
