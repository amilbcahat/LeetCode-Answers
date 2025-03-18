class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        
        return all(count % 2 == 0 for count in freq.values())