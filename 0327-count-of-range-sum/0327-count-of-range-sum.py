class BIT: 
    def __init__(self, nums):
        self.n = len(nums) 
        self.nums = nums
        # +2 for safety: +1 for 1-based indexing, +1 for edge cases in binary search
        self.bit = [0] * (self.n + 2)

    def update(self, index, val): 
        # Convert to 1-based indexing (BIT requirement)
        index += 1
        # Use actual BIT size to avoid out-of-bounds
        while index < len(self.bit): 
            self.bit[index] += val
            # Move to next position using BIT magic: index += (index & -index)
            index += (index & -index)

    def getSum(self, index): 
        # Convert to 1-based indexing
        index += 1
        total = 0
        while index > 0: 
            total += self.bit[index]
            # Move to parent using BIT magic: index -= (index & -index)
            index -= (index & -index)
        return total

    def bs(self, target, sorted_array): 
        """
        Binary search to find FIRST INDEX where sorted_array[index] > target
        This is used for coordinate compression (mapping values to BIT indices)
        """
        l, r = 0, len(sorted_array)
        while l < r: 
            mid = (l + r) // 2  # IMPORTANT: Calculate mid INSIDE the loop
            if sorted_array[mid] > target: 
                r = mid  # Go left (mid might be the answer)
            else: 
                l = mid + 1  # Go right (mid is too small)
        return l


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        
        # STEP 1: Calculate all prefix sums
        pre = [0] * (n + 1)  # pre[0] = 0, then pre[i] = sum of first i elements
        for i in range(n): 
            pre[i + 1] = pre[i] + nums[i]
        
        # STEP 2: Sort prefix sums for coordinate compression
        # We need sorted order to map large values to small BIT indices
        pre.sort()
        
        # STEP 3: Create BIT using the sorted prefix array size
        bit = BIT(pre)
        
        # STEP 4: Process each element left to right
        current_prefix = 0  # Running prefix sum as we iterate
        ans = 0
        
        for i in range(n): 
            # SUBSTEP A: Add CURRENT prefix sum to BIT (for future queries)
            # Find compressed index for current_prefix in sorted array
            compressed_idx = bit.bs(current_prefix, pre)
            # Add 1 to frequency count at this index
            bit.update(compressed_idx, 1)
            
            # SUBSTEP B: Update running prefix sum
            current_prefix += nums[i]
            
            # SUBSTEP C: Count valid subarrays ending at position i
            # We want: lower <= subarray_sum <= upper
            # Since subarray_sum = current_prefix - previous_prefix:
            # lower <= current_prefix - previous_prefix <= upper
            # Rearranging: current_prefix - upper <= previous_prefix <= current_prefix - lower
            
            # Count previous prefix sums in range [current_prefix - upper, current_prefix - lower]
            # Using range counting: count(<=b) - count(<=a-1) gives count in range [a,b]
            
            upper_bound = bit.bs(current_prefix - lower, pre)      # Index for first element > (current_prefix - lower)
            lower_bound = bit.bs(current_prefix - upper - 1, pre)  # Index for first element > (current_prefix - upper - 1)
            
            # CRITICAL: Two separate getSum calls, then subtract
            count_upper = bit.getSum(upper_bound)  # Count of elements <= (current_prefix - lower)
            count_lower = bit.getSum(lower_bound)  # Count of elements <= (current_prefix - upper - 1)
            
            ans += count_upper - count_lower
        
        return ans

# ALGORITHM SUMMARY:
# 1. Use prefix sums to convert subarray problem to "count previous prefixes in range"
# 2. Use coordinate compression (sorting + binary search) to map large values to small indices
# 3. Use BIT to efficiently count frequencies in ranges
# 4. Process array left-to-right, adding current prefix to BIT before querying for next position

# KEY INSIGHTS TO REMEMBER:
# - Add current prefix to BIT BEFORE updating it (timing matters!)
# - Range counting needs TWO separate getSum calls, then subtract
# - Binary search finds "first index > target" for coordinate compression
# - BIT uses 1-based indexing internally (always +1 when converting)