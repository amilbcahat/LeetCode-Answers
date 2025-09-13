class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freMap = Counter(nums)

        curMax = -1
        for key, freq in freMap.items(): 
            if freMap[key] == 1: 
                curMax = max(curMax, key)

        return curMax
