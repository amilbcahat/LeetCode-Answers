class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Hash map to store frequency of prefix counts modulo 'modulo'
        # Initialize with 0 count having frequency 1 (empty subarray)
        preMap = defaultdict(int)
        preMap[0] = 1
        
        # Running count of elements that satisfy nums[i] % modulo == k
        prefix = 0
        
        # Result counter for interesting subarrays
        res = 0
        
        for n in nums:
            # Increment count if current number satisfies the condition
            if n % modulo == k:
                prefix += 1
            
            # Calculate what remainder previous prefix counts should have
            # to form an interesting subarray with current position
            # Formula derived from: (prefix - prevPrefix) % modulo = k
            # Rearranged to: prevPrefix % modulo = (prefix + modulo - k) % modulo
            target = (prefix + modulo - k) % modulo
            
            # Add count of previous positions that form interesting subarrays
            # with current position
            res += preMap[target]
            
            # Store current prefix count's remainder in hash map for future positions
            preMap[prefix % modulo] += 1
            
        return res