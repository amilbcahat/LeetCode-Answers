class BIT: 
    def __init__(self):
        self.maxLength = 0 
        self.frequency = 0

class Solution:
    def getMax(self, index): 
        index += 1
        maxRes = 0
        while index > 0: 
            maxRes = max(maxRes, self.bit[index].maxLength)
            index -= index & - index

        return maxRes

    def getFrequency(self, index, maxLength): 
        index += 1
        res = 0
        while index > 0: 
            if self.bit[index].maxLength == maxLength:
                res += self.bit[index].frequency
            index -= index & - index
        return res

    def update(self, index, maxLength, frequency): 
        index += 1
        while index <= self.n: 
            if self.bit[index].maxLength < maxLength: 
                self.bit[index].maxLength = maxLength
                self.bit[index].frequency = frequency
            elif self.bit[index].maxLength == maxLength: 
                self.bit[index].frequency += frequency
            index += index & -index

    def findNumberOfLIS(self, nums: List[int]) -> int:
        self.n = len(nums)
        self.bit = [BIT() for _ in range(self.n + 1)]
        indicies = list(range(self.n))

        indicies.sort(key=lambda x: ( nums[x], -x))

        for index in indicies: 
            curMax = self.getMax(index)

            if curMax == 0: 
                self.update(index, 1, 1)
                continue

            freq = self.getFrequency(index, curMax )
            self.update(index, curMax + 1, freq)

        maxLength = self.getMax(self.n - 1)
        
        return self.getFrequency(self.n - 1, maxLength)
            

        
        