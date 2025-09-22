class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        res = [0] * 101

        for n in nums: 
            res[n] += 1

        maxFreq = max(res)
        ans = 0
        for freq in res: 
            if freq == maxFreq: 
                ans += (freq)

        return ans