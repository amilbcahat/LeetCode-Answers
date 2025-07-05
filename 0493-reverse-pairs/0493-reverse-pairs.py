class Fen: 
    def __init__(self, n): 
        self.bit = [0] * (n + 1)
        self.n = n + 1  # Store size for bounds checking

    def getSum(self, index):
        # Get cumulative sum from index 0 to index (inclusive)
        index += 1  # Convert to 1-indexed for Fenwick Tree
        res = 0
        while index > 0: 
            res += self.bit[index]
            index -= index & -index  # Remove lowest set bit
        return res 

    def update(self, index, val):
        # Add val to the element at index
        index += 1  # Convert to 1-indexed for Fenwick Tree
        while index < self.n:
            self.bit[index] += val
            index += index & -index  # Add lowest set bit

class Solution:
    def reversePairs(self, nums) -> int:
        n = len(nums)
        if n == 0: 
            return 0 

        # Create doubled values - these will be STORED in Fenwick Tree
        doubleValues = [2 * num for num in nums]

        # COORDINATE COMPRESSION: Include both nums and doubleValues
        # - nums: needed for QUERY operations (must have valid ranks)
        # - doubleValues: needed for UPDATE operations (what we actually store)
        # The Fenwick Tree only stores doubleValues, but queries need nums ranks!
        uniqueValues = sorted(set(nums + doubleValues))

        # Map each unique value to its rank (0-indexed)
        rankMap = {num: i for i, num in enumerate(uniqueValues)}

        fen = Fen(len(rankMap))
        reversedPairCounts = 0
        
        # Process from RIGHT TO LEFT
        # At position i, Fenwick Tree contains all 2*nums[j] where j > i
        for i in range(n - 1, -1, -1): 
            # QUERY: Count how many 2*nums[j] values < nums[i]
            # This gives us count of j > i where nums[i] > 2*nums[j] (reverse pairs!)
            reversedPairCounts += fen.getSum(rankMap[nums[i]] - 1)
            
            # UPDATE: Add 2*nums[i] to Fenwick Tree for future queries
            # This builds up the frequency count of doubled values we've seen
            fen.update(rankMap[2 * nums[i]], 1)

        return reversedPairCounts