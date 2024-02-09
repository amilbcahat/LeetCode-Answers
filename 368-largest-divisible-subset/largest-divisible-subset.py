class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]
        maxLengthSubset = float("-inf")

        for i in range(len(nums) -1 , -1 , -1):
            initial = dp[i]
            biggestLenSubProb = 0 
            for j in range(i + 1 , len(nums)):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0 : 
                    if len(dp[j]) > biggestLenSubProb: 
                        biggestLenSubProb = len(dp[j])
                        dp[i] = initial + dp[j]
                        maxLengthSubset = max(maxLengthSubset , len(dp[i]))

        for n in dp : 
            if len(n) == maxLengthSubset : 
                return n 
        return [nums[0]]
        