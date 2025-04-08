class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)): 
            return 0

        freqMap = Counter(nums)
        k = 0
        for i in range(len(nums)): 
            # print(i, nums[i])
            if (i + 1) % 3 == 0: 
                k += 1
                # print(nums[i + 1:], set(nums[i + 1:]),i,len(set(nums[i + 1:])), len(nums) - i)
                if len(set(nums[i + 1:])) == (len(nums) - i - 1): 
                    print(nums[i + 1:], len(nums) - i - 1)
                    return k 
                


        return k + 1